#!/usr/bin/env python3
"""The 29 tasks added to the original 11 (extended set: 40 tasks).

  tasks_v2.py            merge the tasks into questions.json / public.json (idempotent) and validate them
  tasks_v2.py --check    validate only

Every task has hidden grading data (questions.json), DIFFERENT public examples for the harness verifier (public.json),
and in REFS a known-good answer (must pass both) and known-bad answers (must fail the hidden grader), so a grader
bug is caught before any model is run.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

def rx(id, desc, match, nomatch):
    return {"id": id, "category": "regex", "type": "regex", "match": match, "nomatch": nomatch,
            "prompt": f"Write a single regular expression (Python `re` syntax, to be used with re.fullmatch) that matches {desc} "
                      "Reply with ONLY the regex in a code block, no explanation."}

def py(id, func, text, test):
    return {"id": id, "category": "python", "type": "python", "func": func,
            "prompt": f"Write a Python function `{func}` {text} Reply with ONLY the code in one code block.", "test": test}

def kc(id, text, tokens):
    return {"id": id, "category": "kubectl", "type": "tokens",
            "prompt": f"Give the single kubectl command to {text} Reply with ONLY the command in a code block.", "tokens": tokens}

SCHEMA_EMP = ("Table `employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER)`.")
SCHEMA_ORD = ("Tables `customers(id INTEGER PRIMARY KEY, name TEXT)` and `orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER, placed_on TEXT)` "
              "(`placed_on` is 'YYYY-MM-DD').")
DDL_EMP = "CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, manager_id INTEGER);"
DDL_ORD = ("CREATE TABLE customers(id INTEGER PRIMARY KEY, name TEXT); "
           "CREATE TABLE orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER, placed_on TEXT);")

def sq(id, text, schema, setup, expected, ordered):
    return {"id": id, "category": "sql", "type": "sql", "ordered": ordered, "setup": setup, "expected": expected,
            "prompt": f"{schema} Write one SQLite query that {text} Reply with ONLY the SQL query in a code block."}

def sh(id, text, files, expected, post=None):
    q = {"id": id, "category": "shell", "type": "shell", "files": files, "expected": expected,
         "prompt": f"{text} Reply with ONLY the bash command (a one-liner or pipeline) in a code block."}
    if post: q["post"] = post
    return q

EMP = (DDL_EMP + " INSERT INTO employees VALUES (1,'Gus','hr',90000,NULL),(2,'Bob','eng',60000,7),(3,'Cy','ops',55000,7),"
       "(4,'Dee','ops',70000,3),(5,'Eve','eng',60000,7),(6,'Fay','hr',50000,NULL),(7,'Ann','eng',90000,NULL);")
ORD = (DDL_ORD + " INSERT INTO customers VALUES (1,'Zed'),(2,'Amy'),(3,'Bo'),(4,'Cat');"
       " INSERT INTO orders VALUES (1,1,100,'2024-01-05'),(2,1,50,'2024-01-20'),(3,2,70,'2024-02-11'),(4,2,30,'2023-12-31'),"
       "(5,3,200,'2024-03-01'),(6,3,10,'2024-03-15'),(7,1,5,'2025-01-01');")

TASKS = [
    # ---- regex (5)
    rx("regex-time24", "a 24-hour clock time `HH:MM` with two-digit hours 00-23 and two-digit minutes 00-59.",
       ["00:00", "23:59", "09:05", "12:30"], ["24:00", "12:60", "9:05", "12:5", "23:599", "ab:cd", "7:7"]),
    rx("regex-semver", "a version `MAJOR.MINOR.PATCH` where each part is a non-negative integer without leading zeros (so `0` is allowed, `01` is not).",
       ["0.0.0", "1.2.3", "10.20.30", "100.0.1"], ["01.2.3", "1.02.3", "1.2.03", "1.2", "1.2.3.4", "v1.2.3", "1.2.x", "-1.2.3"]),
    rx("regex-mac", "a MAC address: six pairs of hex digits (either case) separated by colons.",
       ["00:1A:2b:3C:4d:5E", "ff:ff:ff:ff:ff:ff", "01:23:45:67:89:ab"],
       ["00:1A:2b:3C:4d", "00-1A-2b-3C-4d-5E", "00:1A:2b:3C:4d:5G", "00:1A:2b:3C:4d:5E:6F", "0:1A:2b:3C:4d:5E", "001A.2b3C.4d5E"]),
    rx("regex-uuid", "a UUID in canonical form: 8-4-4-4-12 LOWERCASE hex digits separated by hyphens.",
       ["123e4567-e89b-12d3-a456-426614174000", "00000000-0000-0000-0000-000000000000", "ffffffff-ffff-ffff-ffff-ffffffffffff"],
       ["123E4567-e89b-12d3-a456-426614174000", "123e4567e89b12d3a456426614174000", "123e4567-e89b-12d3-a456-42661417400",
        "123e4567-e89b-12d3-a456-4266141740000", "123g4567-e89b-12d3-a456-426614174000", "123e4567-e89b-12d3-a456"]),
    rx("regex-slug", "a URL slug: lowercase letters and digits in words separated by single hyphens, with no leading, trailing or doubled hyphen.",
       ["hello", "hello-world", "a1-b2-c3", "2024-report", "x"], ["Hello", "hello_world", "-hello", "hello-", "hello--world", "hello world", ""]),
    # ---- python (8)
    py("py-parens", "is_balanced(s)", "returning True if the brackets `()`, `[]` and `{}` in the string are balanced and correctly nested, else False. Other characters are ignored; the empty string is balanced.",
       "assert is_balanced('')\nassert is_balanced('()[]{}')\nassert is_balanced('([{}])')\nassert is_balanced('a(b[c]d)e')\nassert not is_balanced('(]')\nassert not is_balanced('((')\n"
       "assert not is_balanced('())')\nassert not is_balanced('{[}]')\nassert not is_balanced(']')\nassert is_balanced('()'*50000)\n"),
    py("py-roman", "to_roman(n)", "converting an integer 1..3999 to its Roman numeral (standard subtractive form, e.g. 4 is IV, 1994 is MCMXCIV).",
       "assert to_roman(1)=='I'\nassert to_roman(4)=='IV'\nassert to_roman(9)=='IX'\nassert to_roman(14)=='XIV'\nassert to_roman(40)=='XL'\nassert to_roman(58)=='LVIII'\n"
       "assert to_roman(90)=='XC'\nassert to_roman(400)=='CD'\nassert to_roman(1994)=='MCMXCIV'\nassert to_roman(3999)=='MMMCMXCIX'\n"),
    py("py-rle", "rle_encode(s)", "that run-length encodes a string: each run of identical characters becomes the character followed by the run length, e.g. 'aaabcc' becomes 'a3b1c2'. The empty string gives ''.",
       "assert rle_encode('')==''\nassert rle_encode('a')=='a1'\nassert rle_encode('aaabcc')=='a3b1c2'\nassert rle_encode('aabbaa')=='a2b2a2'\nassert rle_encode('x'*12)=='x12'\n"
       "assert rle_encode('ab'*3)=='a1b1a1b1a1b1'\n"),
    py("py-flatten", "flatten(x)", "that flattens an arbitrarily nested list of integers into a flat list, keeping the order, e.g. [1,[2,[3]],4] becomes [1,2,3,4]. Nesting can be up to 5000 levels deep.",
       "assert flatten([1,[2,[3,[4]],5]])==[1,2,3,4,5]\nassert flatten([])==[]\nassert flatten([[],[[]]])==[]\nassert flatten([1,2])==[1,2]\n"
       "deep=[7]\nfor _ in range(5000): deep=[deep]\nassert flatten(deep)==[7]\nassert flatten([[1,2],[3,[4,5]],6])==[1,2,3,4,5,6]\n"),
    py("py-twosum", "two_sum(nums, target)", "returning the two indices [i, j] with i < j whose values add up to `target`; exactly one such pair exists. It is tested with 200000 numbers, so it must be O(n).",
       "import time\nassert two_sum([2,7,11,15],9)==[0,1]\nassert two_sum([3,2,4],6)==[1,2]\nassert two_sum([3,3],6)==[0,1]\nassert two_sum([-1,-2,-3,-4,-5],-8)==[2,4]\n"
       "big=list(range(200000))\nt=time.time(); r=two_sum(big,199998+199999); assert time.time()-t<5,'too slow'\nassert r==[199998,199999]\n"),
    py("py-editdist", "edit_distance(a, b)", "returning the Levenshtein edit distance between two strings (insert, delete, replace, each cost 1). It is tested on strings of 1500 characters.",
       "import time,random\nassert edit_distance('kitten','sitting')==3\nassert edit_distance('','abc')==3\nassert edit_distance('abc','abc')==0\nassert edit_distance('flaw','lawn')==2\n"
       "assert edit_distance('intention','execution')==5\nassert edit_distance('abc','')==3\nrandom.seed(3)\na=''.join(random.choice('ab') for _ in range(1500))\nb=''.join(random.choice('ab') for _ in range(1500))\n"
       "t=time.time(); d=edit_distance(a,b); assert time.time()-t<10,'too slow'\nassert 0<d<1500\nassert edit_distance(a,a)==0\n"),
    py("py-spiral", "spiral_order(matrix)", "returning the elements of a rectangular matrix (list of lists) in clockwise spiral order starting at the top-left, e.g. [[1,2],[3,4]] gives [1,2,4,3]. An empty matrix gives [].",
       "assert spiral_order([[1,2,3],[4,5,6],[7,8,9]])==[1,2,3,6,9,8,7,4,5]\nassert spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]])==[1,2,3,4,8,12,11,10,9,5,6,7]\n"
       "assert spiral_order([[1]])==[1]\nassert spiral_order([])==[]\nassert spiral_order([[1],[2],[3]])==[1,2,3]\nassert spiral_order([[1,2,3]])==[1,2,3]\nassert spiral_order([[1,2],[3,4]])==[1,2,4,3]\n"),
    py("py-sieve", "count_primes(n)", "returning how many prime numbers are <= n (n may be 0 or 1). It is tested with n = 3,000,000, so trial division is too slow.",
       "import time\nassert count_primes(0)==0\nassert count_primes(1)==0\nassert count_primes(2)==1\nassert count_primes(10)==4\nassert count_primes(97)==25\nassert count_primes(100)==25\n"
       "assert count_primes(1000)==168\nt=time.time(); r=count_primes(3000000); assert time.time()-t<5,'too slow'\nassert r==216816\n"),
    # ---- kubectl (6)
    kc("kubectl-label-selector", "list the pods labelled `app=web` in namespace `prod`.",
       [["kubectl"], ["get"], ["\\b(pods?|po)\\b"], ["(-l[ =]?|--selector[ =])app=web\\b"], ["-n[ =]?prod\\b", "--namespace[ =]prod\\b"]]),
    kc("kubectl-rollout-restart", "restart the deployment `api` in namespace `prod` with a rolling restart.",
       [["kubectl"], ["rollout"], ["restart"], ["deploy(ment)?[/ ]api\\b"], ["-n[ =]?prod\\b", "--namespace[ =]prod\\b"]]),
    kc("kubectl-exec", "run the command `ls /data` in the container `db` of the pod `db-0` in namespace `data`.",
       [["kubectl"], ["exec"], ["\\bdb-0\\b"], ["-c[ =]?db\\b", "--container[ =]db\\b"], ["-n[ =]?data\\b", "--namespace[ =]data\\b"], ["--\\s+ls\\s+/data\\b"]]),
    kc("kubectl-portforward", "forward local port 8080 to port 80 of the service `web` in namespace `staging`.",
       [["kubectl"], ["port-forward"], ["\\b(svc|service)/web\\b"], ["\\b8080:80\\b"], ["-n[ =]?staging\\b", "--namespace[ =]staging\\b"]]),
    kc("kubectl-events-sorted", "list the events in namespace `prod` sorted by their last timestamp.",
       [["kubectl"], ["get"], ["\\bevents?\\b"], ["-n[ =]?prod\\b", "--namespace[ =]prod\\b"], ["--sort-by[ =]\\S*lastTimestamp\\b"]]),
    kc("kubectl-top", "show the CPU and memory usage of the pods in namespace `prod`, sorted by memory.",
       [["kubectl"], ["top"], ["\\b(pods?|po)\\b"], ["-n[ =]?prod\\b", "--namespace[ =]prod\\b"], ["--sort-by[ =]memory\\b"]]),
    # ---- sql (5)
    sq("sql-top-earners", "returns the names of employees who earn more than 60000, highest salary first, ties broken by name alphabetically.", SCHEMA_EMP, EMP,
       [["Ann"], ["Gus"], ["Dee"]], True),
    sq("sql-dept-stats", "returns, for every department, the department name, the number of employees and the total salary, ordered by department name.", SCHEMA_EMP, EMP,
       [["eng", 3, 210000], ["hr", 2, 140000], ["ops", 2, 125000]], True),
    sq("sql-no-orders", "returns the names of customers who have placed no orders, ordered by name.", SCHEMA_ORD, ORD, [["Cat"]], True),
    sq("sql-second-salary", "returns the second highest DISTINCT salary as a single value.", SCHEMA_EMP, EMP, [[70000]], False),
    sq("sql-monthly", "returns the total order amount per month (as 'YYYY-MM') for orders placed in 2024, only for months that have orders, ordered by month.",
       SCHEMA_ORD, ORD, [["2024-01", 150], ["2024-02", 70], ["2024-03", 210]], True),
    # ---- shell (5)
    sh("sh-count-errors", "The file `app.log` is in the current directory. Print the number of lines that contain the exact word ERROR (uppercase), and nothing else.",
       {"app.log": "INFO start\nERROR disk full\nWARN slow\nERROR timeout\nINFO error handled\nERROR again\nDEBUG ERRORS ignored? no\n"}, "3"),
    sh("sh-top-ips", "The file `access.log` has an IP address as the first space-separated field of each line. Print the 3 most frequent IP addresses with their counts, one per line as `COUNT IP`, "
       "most frequent first, ties broken by IP address in ascending string order.",
       {"access.log": "10.0.0.2 GET /\n10.0.0.1 GET /a\n10.0.0.2 GET /b\n10.0.0.3 GET /\n10.0.0.1 GET /c\n10.0.0.2 POST /d\n10.0.0.9 GET /\n10.0.0.3 GET /x\n"},
       "3 10.0.0.2\n2 10.0.0.1\n2 10.0.0.3"),
    sh("sh-csv-sum", "The file `sales.csv` is comma-separated with a header line. Print the sum of the third column over all data rows, and nothing else.",
       {"sales.csv": "id,item,qty\n1,pen,10\n2,ink,5\n3,pad,7\n4,cap,20\n"}, "42"),
    sh("sh-rename-ext", "The current directory contains some `.txt` files and other files. Rename every `.txt` file to the same name with the extension `.md`.",
       {"a.txt": "1", "b.txt": "2", "notes.bak": "3", "c.txt": "4"}, "a.md\nb.md\nc.md\nnotes.bak", post="ls"),
    sh("sh-distinct-words", "The file `text.txt` contains words separated by spaces and newlines. Print the number of distinct words, ignoring case, and nothing else.",
       {"text.txt": "The quick brown fox\njumps over the lazy dog\nTHE DOG barks\n"}, "9"),
]

# public examples: a DIFFERENT fixture / strings from the hidden ones; kubectl tasks carry a structured intent
PUBLIC = {
    "regex-time24": {"match": ["01:15", "18:45", "20:00"], "nomatch": ["25:10", "10:75", "1:15", "10:5"]},
    "regex-semver": {"match": ["2.0.15", "0.10.0", "7.7.7"], "nomatch": ["3.04.5", "4.5", "1.2.3.4.5", "10.0.00"]},
    "regex-mac": {"match": ["aa:bb:cc:dd:ee:ff", "12:34:56:78:9A:BC"], "nomatch": ["12:34:56:78:9A", "12:34:56:78:9A:BG", "12-34-56-78-9A-BC"]},
    "regex-uuid": {"match": ["550e8400-e29b-41d4-a716-446655440000", "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"],
                   "nomatch": ["550E8400-e29b-41d4-a716-446655440000", "550e8400-e29b-41d4-a716", "550e8400e29b41d4a716446655440000"]},
    "regex-slug": {"match": ["my-first-post", "v2", "a-b-c"], "nomatch": ["My-Post", "post-", "a--b", "a b"]},
    "py-parens": {"func": "is_balanced", "cases": [["is_balanced('{[()]}')", "True"], ["is_balanced('([)]')", "False"], ["is_balanced('x')", "True"], ["is_balanced('}{')", "False"]]},
    "py-roman": {"func": "to_roman", "cases": [["to_roman(3)", "'III'"], ["to_roman(49)", "'XLIX'"], ["to_roman(2024)", "'MMXXIV'"], ["to_roman(900)", "'CM'"]]},
    "py-rle": {"func": "rle_encode", "cases": [["rle_encode('wwwwb')", "'w4b1'"], ["rle_encode('abc')", "'a1b1c1'"], ["rle_encode('')", "''"]]},
    "py-flatten": {"func": "flatten", "cases": [["flatten([[1],[2,[3]]])", "[1,2,3]"], ["flatten([])", "[]"], ["flatten([[[[9]]]])", "[9]"]],
                   "perf": "d=[1]\nfor _ in range(3000): d=[d]\nflatten(d)", "perf_limit": 2.0, "perf_label": "3000 nested levels"},
    "py-twosum": {"func": "two_sum", "cases": [["two_sum([1,5,9],14)", "[1,2]"], ["two_sum([4,4],8)", "[0,1]"], ["two_sum([0,4,3,0],0)", "[0,3]"]],
                  "perf": "n=list(range(50000))\ntwo_sum(n,49998+49999)", "perf_limit": 2.0, "perf_label": "50,000 numbers"},
    "py-editdist": {"func": "edit_distance", "cases": [["edit_distance('horse','ros')", "3"], ["edit_distance('a','a')", "0"], ["edit_distance('abc','xyz')", "3"]],
                    "perf": "edit_distance('ab'*400,'ba'*400)", "perf_limit": 4.0, "perf_label": "800-character strings"},
    "py-spiral": {"func": "spiral_order", "cases": [["spiral_order([[1,2],[3,4],[5,6]])", "[1,2,4,6,5,3]"], ["spiral_order([[5]])", "[5]"], ["spiral_order([[1,2,3],[4,5,6]])", "[1,2,3,6,5,4]"]]},
    "py-sieve": {"func": "count_primes", "cases": [["count_primes(30)", "10"], ["count_primes(3)", "2"], ["count_primes(1)", "0"]],
                 "perf": "count_primes(500000)", "perf_limit": 2.0, "perf_label": "n = 500,000"},
    "kubectl-label-selector": {"intent": {"verb": "get", "kind": "pods", "namespace": "prod", "flags": {"selector": "app=web"}}},
    "kubectl-rollout-restart": {"intent": {"verb": "rollout", "args_head": ["restart"], "kind": "deployment", "name": "api", "namespace": "prod"}},
    "kubectl-exec": {"intent": {"verb": "exec", "name": "db-0", "namespace": "data", "flags": {"container": "db"}, "dashdash": ["ls", "/data"]}},
    "kubectl-portforward": {"intent": {"verb": "port-forward", "namespace": "staging", "target": "web", "target_kinds": ["svc", "service"], "ports": "8080:80"}},
    "kubectl-events-sorted": {"intent": {"verb": "get", "kind": "events", "namespace": "prod", "flags": {"sort-by": ".lastTimestamp"}}},
    "kubectl-top": {"intent": {"verb": "top", "kind": "pods", "namespace": "prod", "flags": {"sort-by": "memory"}}},
    "sql-top-earners": {"setup": DDL_EMP + " INSERT INTO employees VALUES (1,'Kim',NULL,80000,NULL),(2,'Lee',NULL,55000,1),(3,'Max',NULL,80000,1),(4,'Ned',NULL,61000,1);",
                        "expected": [["Kim"], ["Max"], ["Ned"]], "ordered": True},
    "sql-dept-stats": {"setup": DDL_EMP + " INSERT INTO employees VALUES (1,'a','x',10,NULL),(2,'b','x',20,1),(3,'c','y',5,1);",
                       "expected": [["x", 2, 30], ["y", 1, 5]], "ordered": True},
    "sql-no-orders": {"setup": DDL_ORD + " INSERT INTO customers VALUES (1,'Q'),(2,'R'),(3,'S'); INSERT INTO orders VALUES (1,2,10,'2024-05-05');",
                      "expected": [["Q"], ["S"]], "ordered": True},
    "sql-second-salary": {"setup": DDL_EMP + " INSERT INTO employees VALUES (1,'a',NULL,300,NULL),(2,'b',NULL,300,1),(3,'c',NULL,200,1),(4,'d',NULL,100,1);",
                          "expected": [[200]], "ordered": False},
    "sql-monthly": {"setup": DDL_ORD + " INSERT INTO customers VALUES (1,'Q'); INSERT INTO orders VALUES (1,1,5,'2024-07-01'),(2,1,6,'2024-07-30'),(3,1,9,'2024-09-09'),(4,1,100,'2023-07-07');",
                    "expected": [["2024-07", 11], ["2024-09", 9]], "ordered": True},
    "sh-count-errors": {"files": {"app.log": "ERROR a\nok\nERROR b\nERROR c\nERROR d\nwarn\n"}, "expected": "4"},
    "sh-top-ips": {"files": {"access.log": "1.1.1.1 a\n2.2.2.2 b\n1.1.1.1 c\n3.3.3.3 d\n2.2.2.2 e\n1.1.1.1 f\n4.4.4.4 g\n"}, "expected": "3 1.1.1.1\n2 2.2.2.2\n1 3.3.3.3"},
    "sh-csv-sum": {"files": {"sales.csv": "id,item,qty\n1,a,1\n2,b,2\n3,c,3\n"}, "expected": "6"},
    "sh-rename-ext": {"files": {"x.txt": "1", "y.txt": "2", "z.doc": "3"}, "expected": "x.md\ny.md\nz.doc", "post": "ls"},
    "sh-distinct-words": {"files": {"text.txt": "Red green\nblue RED\nGreen\n"}, "expected": "3"},
}

# known-good answer (passes hidden AND public) and known-bad answers (fail hidden) for every new task
REFS = {
    "regex-time24": ("```\n([01]\\d|2[0-3]):[0-5]\\d\n```", ["```\n\\d\\d:\\d\\d\n```", "```\n([01]?\\d|2[0-3]):[0-5]\\d\n```"]),
    "regex-semver": ("```\n(0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)\n```", ["```\n\\d+\\.\\d+\\.\\d+\n```", "```\n\\d+\\.\\d+\\.\\d+\\.\\d+\n```"]),
    "regex-mac": ("```\n([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\n```", ["```\n([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\n```", "```\n([0-9a-f]{2}:){5}[0-9a-f]{2}\n```"]),
    "regex-uuid": ("```\n[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\n```", ["```\n[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\n```"]),
    "regex-slug": ("```\n[a-z0-9]+(-[a-z0-9]+)*\n```", ["```\n[a-z0-9-]+\n```", "```\n[a-z0-9]+(-[a-z0-9]+)*-?\n```"]),
    "py-parens": ("```python\ndef is_balanced(s):\n    pairs = {')': '(', ']': '[', '}': '{'}\n    st = []\n    for c in s:\n        if c in '([{':\n            st.append(c)\n        elif c in pairs:\n"
                  "            if not st or st.pop() != pairs[c]:\n                return False\n    return not st\n```",
                  ["```python\ndef is_balanced(s):\n    return s.count('(') == s.count(')')\n```"]),
    "py-roman": ("```python\ndef to_roman(n):\n    out = ''\n    for v, r in [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]:\n"
                 "        while n >= v:\n            out += r; n -= v\n    return out\n```",
                 ["```python\ndef to_roman(n):\n    out = ''\n    for v, r in [(1000,'M'),(500,'D'),(100,'C'),(50,'L'),(10,'X'),(5,'V'),(1,'I')]:\n        while n >= v:\n            out += r; n -= v\n    return out\n```"]),
    "py-rle": ("```python\ndef rle_encode(s):\n    out, i = [], 0\n    while i < len(s):\n        j = i\n        while j < len(s) and s[j] == s[i]:\n            j += 1\n        out.append(s[i] + str(j - i)); i = j\n    return ''.join(out)\n```",
               ["```python\ndef rle_encode(s):\n    from collections import Counter\n    return ''.join(c + str(n) for c, n in Counter(s).items())\n```"]),
    "py-flatten": ("```python\ndef flatten(x):\n    out, stack = [], [iter(x)]\n    while stack:\n        for v in stack[-1]:\n            if isinstance(v, list):\n                stack.append(iter(v)); break\n            out.append(v)\n        else:\n            stack.pop()\n    return out\n```",
                   ["```python\ndef flatten(x):\n    out = []\n    for v in x:\n        if isinstance(v, list): out += flatten(v)\n        else: out.append(v)\n    return out\n```"]),
    "py-twosum": ("```python\ndef two_sum(nums, target):\n    seen = {}\n    for i, v in enumerate(nums):\n        if target - v in seen:\n            return [seen[target - v], i]\n        seen[v] = i\n```",
                  ["```python\ndef two_sum(nums, target):\n    for i in range(len(nums)):\n        for j in range(i + 1, len(nums)):\n            if nums[i] + nums[j] == target:\n                return [i, j]\n```"]),
    "py-editdist": ("```python\ndef edit_distance(a, b):\n    prev = list(range(len(b) + 1))\n    for i, ca in enumerate(a, 1):\n        cur = [i]\n        for j, cb in enumerate(b, 1):\n            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))\n        prev = cur\n    return prev[-1]\n```",
                    ["```python\ndef edit_distance(a, b):\n    return abs(len(a) - len(b))\n```"]),
    "py-spiral": ("```python\ndef spiral_order(matrix):\n    m = [list(r) for r in matrix]\n    out = []\n    while m:\n        out += m.pop(0)\n        m = [list(r) for r in zip(*m)][::-1]\n    return out\n```",
                  ["```python\ndef spiral_order(matrix):\n    return [x for r in matrix for x in r]\n```"]),
    "py-sieve": ("```python\ndef count_primes(n):\n    if n < 2:\n        return 0\n    s = bytearray([1]) * (n + 1)\n    s[0] = s[1] = 0\n    for i in range(2, int(n ** 0.5) + 1):\n        if s[i]:\n            s[i*i::i] = bytearray(len(s[i*i::i]))\n    return sum(s)\n```",
                 ["```python\ndef count_primes(n):\n    c = 0\n    for k in range(2, n + 1):\n        if all(k % d for d in range(2, int(k ** 0.5) + 1)):\n            c += 1\n    return c\n```"]),
    "kubectl-label-selector": ("```\nkubectl get pods -l app=web -n prod\n```", ["```\nkubectl get pods -n prod\n```", "```\nkubectl get pods -l app=web\n```"]),
    "kubectl-rollout-restart": ("```\nkubectl rollout restart deployment/api -n prod\n```", ["```\nkubectl delete deployment api -n prod\n```", "```\nkubectl rollout restart deployment/api\n```"]),
    "kubectl-exec": ("```\nkubectl exec db-0 -c db -n data -- ls /data\n```", ["```\nkubectl exec db-0 -n data -- ls /data\n```", "```\nkubectl exec db-0 -c db -n data ls /data\n```"]),
    "kubectl-portforward": ("```\nkubectl port-forward svc/web 8080:80 -n staging\n```", ["```\nkubectl port-forward web 8080:80 -n staging\n```", "```\nkubectl port-forward svc/web 80:8080 -n staging\n```"]),
    "kubectl-events-sorted": ("```\nkubectl get events -n prod --sort-by=.lastTimestamp\n```", ["```\nkubectl get events -n prod\n```", "```\nkubectl get events -n prod --sort-by=.metadata.creationTimestamp\n```"]),
    "kubectl-top": ("```\nkubectl top pods -n prod --sort-by=memory\n```", ["```\nkubectl top pods -n prod --sort-by=cpu\n```", "```\nkubectl get pods -n prod --sort-by=memory\n```"]),
    "sql-top-earners": ("```sql\nSELECT name FROM employees WHERE salary > 60000 ORDER BY salary DESC, name;\n```",
                        ["```sql\nSELECT name FROM employees WHERE salary >= 60000 ORDER BY salary DESC, name;\n```", "```sql\nSELECT name FROM employees WHERE salary > 60000 ORDER BY salary DESC;\n```"]),
    "sql-dept-stats": ("```sql\nSELECT dept, COUNT(*), SUM(salary) FROM employees GROUP BY dept ORDER BY dept;\n```", ["```sql\nSELECT dept, COUNT(*), AVG(salary) FROM employees GROUP BY dept ORDER BY dept;\n```"]),
    "sql-no-orders": ("```sql\nSELECT c.name FROM customers c LEFT JOIN orders o ON o.customer_id = c.id WHERE o.id IS NULL ORDER BY c.name;\n```",
                      ["```sql\nSELECT c.name FROM customers c JOIN orders o ON o.customer_id = c.id ORDER BY c.name;\n```"]),
    "sql-second-salary": ("```sql\nSELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;\n```", ["```sql\nSELECT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;\n```"]),
    "sql-monthly": ("```sql\nSELECT strftime('%Y-%m', placed_on) AS m, SUM(amount) FROM orders WHERE placed_on >= '2024-01-01' AND placed_on < '2025-01-01' GROUP BY m ORDER BY m;\n```",
                    ["```sql\nSELECT strftime('%Y-%m', placed_on) AS m, SUM(amount) FROM orders GROUP BY m ORDER BY m;\n```"]),
    "sh-count-errors": ("```bash\ngrep -cw ERROR app.log\n```", ["```bash\ngrep -ci error app.log\n```", "```bash\ngrep ERROR app.log\n```"]),
    "sh-top-ips": ("```bash\nawk '{print $1}' access.log | sort | uniq -c | sort -k1,1nr -k2,2 | head -3\n```", ["```bash\nawk '{print $1}' access.log | sort | uniq -c | sort -nr | head -3\n```"]),
    "sh-csv-sum": ("```bash\nawk -F, 'NR>1{s+=$3} END{print s}' sales.csv\n```", ["```bash\nawk -F, 'NR>1{s+=$2} END{print s}' sales.csv\n```"]),
    "sh-rename-ext": ("```bash\nfor f in *.txt; do mv \"$f\" \"${f%.txt}.md\"; done\n```", ["```bash\nfor f in *; do mv \"$f\" \"${f%.*}.md\"; done\n```"]),
    "sh-distinct-words": ("```bash\ntr -s ' \\n' '\\n\\n' < text.txt | tr 'A-Z' 'a-z' | sort -u | wc -l\n```", ["```bash\nwc -w < text.txt\n```"]),
}

def merge():
    qp, pp = f"{HERE}/questions.json", f"{HERE}/public.json"
    mine = {q["id"]: q for q in TASKS}
    qs = [mine.pop(q["id"], q) for q in json.load(open(qp))] + list(mine.values())   # replace by id, append the rest
    json.dump(qs, open(qp, "w"), indent=1, ensure_ascii=False)
    pub = json.load(open(pp)); pub.update(PUBLIC)
    json.dump(pub, open(pp, "w"), indent=1, ensure_ascii=False)
    print(f"{len(TASKS)} tasks merged; {len(qs)} tasks in questions.json")

def validate():
    import run as base
    import repeat
    qs = {q["id"]: q for q in json.load(open(f"{HERE}/questions.json"))}
    bad = 0
    for id, (good, wrongs) in REFS.items():
        q = qs[id]
        ok, why = base.check(q, good)
        if not ok: print(f"FAIL good answer rejected by hidden grader: {id}: {why}"); bad += 1
        vok, vwhy = repeat.verify(q, good)
        if not vok: print(f"FAIL good answer rejected by public verifier: {id}: {vwhy}"); bad += 1
        for w in wrongs:
            ok, why = base.check(q, w)
            if ok: print(f"FAIL wrong answer accepted by hidden grader: {id}: {w!r}"); bad += 1
    print(f"validated {len(REFS)} tasks, {bad} problems")
    return bad

if __name__ == "__main__":
    if "--check" not in sys.argv: merge()
    raise SystemExit(1 if validate() else 0)
