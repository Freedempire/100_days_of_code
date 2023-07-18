# Regular Expression HOWTO

[Reference link](https://docs.python.org/3/howto/regex.html)

## Introduction

Regular expressions (called REs, or regexes, or regex patterns) are essentially a tiny, highly specialized programming language embedded inside Python and made available through the [re](https://docs.python.org/3/library/re.html#module-re) module. Using this little language, you specify the rules for the set of possible strings that you want to match; this set might contain English sentences, or e-mail addresses, or TeX commands, or anything you like. You can then ask questions such as “Does this string match the pattern?”, or “Is there a match for the pattern anywhere in this string?”. You can also use REs to modify a string or to split it apart in various ways.

Regular expression patterns are compiled into a series of bytecodes which are then executed by a matching engine written in C. For advanced use, it may be necessary to pay careful attention to how the engine will execute a given RE, and write the RE in a certain way in order to produce bytecode that runs faster.

The regular expression language is relatively small and restricted, so not all possible string processing tasks can be done using regular expressions. There are also tasks that can be done with regular expressions, but the expressions turn out to be very complicated. In these cases, you may be better off writing Python code to do the processing; while Python code will be slower than an elaborate regular expression, it will also probably be more understandable.

## Simple Patterns

### Matching Characters

Most letters and characters will simply match themselves. For example, the regular expression `test` will match the string `test` exactly. (You can enable a case-insensitive mode that would let this RE match `Test` or `TEST` as well.)

Some characters are special *metacharacters*, and don’t match themselves. Instead, they signal that some out-of-the-ordinary thing should be matched, or they affect other portions of the RE by repeating them or changing their meaning.

Here’s a complete list of the metacharacters; their meanings will be discussed in the rest of this HOWTO.

```re
. ^ $ * + ? { } [ ] \ | ( )
```

The first metacharacters we’ll look at are `[` and `]`. They’re used for specifying a *character class*, which is a *set* of characters that you wish to match. Characters can be listed individually, or a *range* of characters can be indicated by giving two characters and separating them by a `'-'`. For example, `[abc]` will match any of the characters `a`, `b`, or `c`; this is the same as `[a-c]`, which uses a range to express the same set of characters. If you wanted to match only lowercase letters, your RE would be `[a-z]`.

Metacharacters (except `\`) are *not* active inside classes. For example, `[akm$]` will match any of the characters `'a'`, `'k'`, `'m'`, or `'$'`.

You can match the characters not listed within the class by *complementing* the set. This is indicated by including a `'^'` as the first character of the class. For example, `[^5]` will match any character except `'5'`. If the caret appears elsewhere in a character class, it does not have special meaning. For example: `[5^]` will match either a `'5'` or a `'^'`.

Perhaps the most important metacharacter is the backslash, `\`. As in Python string literals, the backslash can be followed by various characters to *signal* various special sequences. It’s also used to *escape* all the metacharacters so you can still match them in patterns; for example, if you need to match a `[` or `\`, you can precede them with a backslash to remove their special meaning: `\[` or `\\`.

Some of the special sequences beginning with `'\'` represent predefined sets of characters that are often useful, such as the set of digits, the set of letters, or the set of anything that isn’t whitespace.

Let’s take an example: `\w` matches any alphanumeric character. If the regex pattern is expressed in bytes, this is equivalent to the class `[a-zA-Z0-9_]`. If the regex pattern is a string, `\w` will match all the characters marked as letters in the Unicode database provided by the [unicodedata](https://docs.python.org/3/library/unicodedata.html#module-unicodedata) module. You can use the more restricted definition of `\w` in a string pattern by supplying the [re.ASCII](https://docs.python.org/3/library/re.html#re.ASCII) flag when compiling the regular expression.

The following list of special sequences isn’t complete. For a complete list of sequences and expanded class definitions for Unicode string patterns, see the last part of [Regular Expression Syntax](https://docs.python.org/3/library/re.html#re-syntax) in the Standard Library reference. In general, the Unicode versions match any character that’s in the appropriate category in the Unicode database.

* `\d`
    Matches any decimal digit; this is equivalent to the class `[0-9]`.

* `\D`
    Matches any non-digit character; this is equivalent to the class `[^0-9]`.

* `\s`
    Matches any whitespace character; this is equivalent to the class `[ \t\n\r\f\v]`.

* `\S`
    Matches any non-whitespace character; this is equivalent to the class `[^ \t\n\r\f\v]`.

* `\w`
    Matches any alphanumeric character; this is equivalent to the class `[a-zA-Z0-9_]`.

* `\W`
    Matches any non-alphanumeric character; this is equivalent to the class `[^a-zA-Z0-9_]`.

These sequences can be included inside a character class. For example, `[\s,.]` is a character class that will match any whitespace character, or `','` or `'.'`.

The final metacharacter in this section is `.`. It matches anything *except* a *newline character*, and there’s an alternate mode ([re.DOTALL](https://docs.python.org/3/library/re.html#re.DOTALL)) where it will match even a newline. `.` is often used where you want to match “any character”.

### Repeating Things

Another capability of regexes is that you can specify that portions of the RE must be repeated a certain number of times.

The first metacharacter for repeating things that we’ll look at is `*`. `*` doesn’t match the literal character `'*'`; instead, it specifies that the previous character can be matched *zero or more times*, instead of exactly once.

For example, `ca*t` will match `'ct'` (0 `'a'` characters), `'cat'` (1 `'a'`), `'caaat'` (3 `'a'` characters), and so forth.

Repetitions such as `*` are *greedy*; when repeating a RE, the matching engine will try to repeat it as many times as possible. If later portions of the pattern don’t match, the matching engine will then back up and try again with fewer repetitions.

Another repeating metacharacter is `+`, which matches *one or more times*. To use a similar example, `ca+t` will match `'cat'` (1 `'a'`), `'caaat'` (3 `'a'`s), but won’t match `'ct'`.

There are two more repeating operators or **quantifiers**. The question mark character, `?`, matches either *once or zero times*; you can think of it as marking something as being *optional*. For example, `home-?brew` matches either `'homebrew'` or `'home-brew'`.

The most complicated quantifier is `{m,n}`, where *m* and *n* are decimal integers. This quantifier means there must be at least *m* repetitions, and at most *n*. For example, `a/{1,3}b` will match `'a/b'`, `'a//b'`, and `'a///b'`. It won’t match `'ab'`, which has no slashes, or `'a////b'`, which has four.

You can omit either *m* or *n*; in that case, a reasonable value is assumed for the missing value. Omitting *m* is interpreted as a lower limit of 0, while omitting *n* results in an upper bound of infinity.

Readers of a reductionist bent may notice that the three other quantifiers can all be expressed using this notation. `{0,}` is the same as `*`, `{1,}` is equivalent to `+`, and `{0,1}` is the same as `?`. It’s better to use `*`, `+`, or `?` when you can, simply because they’re shorter and easier to read.

## Using Regular Expressions

The [re](https://docs.python.org/3/library/re.html#module-re) module provides an interface to the regular expression engine, allowing you to *compile REs into objects and then perform matches with them*.

### Compiling Regular Expressions

Regular expressions are compiled into pattern objects, which have methods for various operations such as searching for pattern matches or performing string substitutions.

```sh
>>> import re
>>> p = re.compile('ab*')
>>> p
re.compile('ab*')
```

[re.compile()](https://docs.python.org/3/library/re.html#re.compile) also accepts an optional *flags* argument, used to enable various special features and syntax variations.

```sh
>>> p = re.compile('ab*', re.IGNORECASE)
```

The RE is passed to [re.compile()](https://docs.python.org/3/library/re.html#re.compile) as a string. REs are handled as strings because regular expressions aren’t part of the core Python language, and no special syntax was created for expressing them. Instead, the [re](https://docs.python.org/3/library/re.html#module-re) module is simply a C extension module included with Python, just like the socket or zlib modules.

### The Backslash Plague

As stated earlier, regular expressions use the backslash character (`'\'`) to indicate special forms or to allow special characters to be used without invoking their special meaning. This conflicts with Python’s usage of the same character for the same purpose in string literals.

Let’s say you want to write a RE that matches the string `\section`, which might be found in a LaTeX file. To figure out what to write in the program code, start with the desired string to be matched. Next, you must escape any backslashes and other metacharacters by preceding them with a backslash, resulting in the string `\\section`. The resulting string that must be passed to [re.compile()](https://docs.python.org/3/library/re.html#re.compile) must be `\\section`. However, to express this as a Python string literal, both backslashes must be escaped again.

In short, to match a literal backslash, one has to write `'\\\\'` as the RE string, because the regular expression must be `\\`, and each backslash must be expressed as `\\` inside a regular Python string literal.

The solution is to use Python’s *raw string notation* for regular expressions; backslashes are not handled in any special way in a string literal prefixed with `'r'`, so `r"\n"` is a two-character string containing `'\'` and `'n'`, while `"\n"` is a one-character string containing a newline.

### Performing Matches

Once you have an object representing a compiled regular expression, what do you do with it? Pattern objects have several methods and attributes.

[match()](https://docs.python.org/3/library/re.html#re.Pattern.match) and [search()](https://docs.python.org/3/library/re.html#re.Pattern.search) return `None` if no match can be found. If they’re successful, a match object instance is returned, containing information about the match: where it starts and ends, the substring it matched, and more.

You can learn about this by interactively experimenting with the [re](https://docs.python.org/3/library/re.html#re.Pattern.search) module. If you have [tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter) available, you may also want to look at [Tools/demo/redemo.py](https://github.com/python/cpython/tree/3.11/Tools/demo/redemo.py), a demonstration program included with the Python distribution. It allows you to enter REs and strings, and displays whether the RE matches or fails.

This HOWTO uses the standard Python interpreter for its examples. First, run the Python interpreter, import the re module, and compile a RE:

```sh
>>> import re
>>> p = re.compile('[a-z]+')
>>> p
re.compile('[a-z]+')
>>> p.match("")
>>> print(p.match(""))
None
>>> m = p.match('tempo')
>>> m
<re.Match object; span=(0, 5), match='tempo'>
>>> m.group()
'tempo'
>>> m.start(), m.end()
(0, 5)
>>> m.span()
(0, 5)
>>> print(p.match('::: message'))
None
>>> m = p.search('::: message'); print(m)
<re.Match object; span=(4, 11), match='message'>
>>> m.group()
'message'
>>> m.span()
(4, 11)
```

[group()](https://docs.python.org/3/library/re.html#re.Match.group) returns the substring that was matched by the RE. [start()](https://docs.python.org/3/library/re.html#re.Match.start) and [end()](https://docs.python.org/3/library/re.html#re.Match.end) return the starting and ending index of the match. [span()](https://docs.python.org/3/library/re.html#re.Match.span) returns both start and end indexes in a single tuple. Since the [match()](https://docs.python.org/3/library/re.html#re.Pattern.match) method only checks if the RE matches at the start of a string, start() will *always be zero*. However, the [search()](https://docs.python.org/3/library/re.html#re.Pattern.search) method of patterns scans through the string, so the match may not start at zero in that case.

Two pattern methods return all of the matches for a pattern. [findall()](https://docs.python.org/3/library/re.html#re.Pattern.findall) returns a list of matching strings:

```sh
>>> p = re.compile(r'\d+')
>>> p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
['12', '11', '10']
```

[findall()](https://docs.python.org/3/library/re.html#re.Pattern.findall) has to create the entire list before it can be returned as the result. The [finditer()](https://docs.python.org/3/library/re.html#re.Pattern.finditer) method returns a sequence of match object instances as an iterator:

```sh
>>> iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
>>> iterator  
<callable_iterator object at 0x...>
>>> for match in iterator:
...     print(match.span())
...
(0, 2)
(22, 24)
(29, 31)
```

### Module-Level Functions

You don’t have to create a pattern object and call its methods; the re module also provides top-level functions called [match()](https://docs.python.org/3/library/re.html#re.match), [search()](https://docs.python.org/3/library/re.html#re.search), [findall()](https://docs.python.org/3/library/re.html#re.findall), [sub()](https://docs.python.org/3/library/re.html#re.sub), and so forth. These functions take the same arguments as the corresponding pattern method with the RE string added as the first argument, and still return either None or a match object instance.

```sh
>>> print(re.match(r'From\s+', 'Fromage amk'))
None
>>> re.match(r'From\s+', 'From amk Thu May 14 19:12:10 1998')  
<re.Match object; span=(0, 5), match='From '>
```

*Under the hood, these functions simply create a pattern object for you and call the appropriate method on it.* They also store the compiled object in a cache, so future calls using the same RE won’t need to parse the pattern again and again.

Should you use these module-level functions, or should you get the pattern and call its methods yourself? If you’re accessing a regex within a loop, pre-compiling it will save a few function calls. Outside of loops, there’s not much difference thanks to the internal cache.

### Compilation Flags

Compilation flags let you modify some aspects of how regular expressions work. Flags are available in the [re](https://docs.python.org/3/library/re.html#module-re) module under two names, a long name such as IGNORECASE and a short, one-letter form such as I. (If you’re familiar with Perl’s pattern modifiers, the one-letter forms use the same letters; the short form of [re.VERBOSE](https://docs.python.org/3/library/re.html#re.VERBOSE) is [re.X](https://docs.python.org/3/library/re.html#re.X), for example.) Multiple flags can be specified by *bitwise OR*-ing them; `re.I | re.M` sets both the I and M flags, for example.

Here’s a table of the available flags, followed by a more detailed explanation of each one.

Flag|Meaning
---|---
ASCII, A|Makes several escapes like `\w`, `\b`, `\s` and `\d` match only on ASCII characters with the respective property.
DOTALL, S|Make `.` match any character, including newlines.
IGNORECASE, I|Do case-insensitive matches.
LOCALE, L|Do a locale-aware match.
MULTILINE, M|Multi-line matching, affecting `^` and `$`.
VERBOSE, X (for ‘extended’)|Enable verbose REs, which can be organized more cleanly and understandably. When this flag has been specified, whitespace within the RE string is ignored, except when the whitespace is in a character class or preceded by an unescaped backslash. This flag also lets you put comments within a RE that will be ignored by the engine; comments are marked by a '#' that’s neither in a character class or preceded by an unescaped backslash.

For example, here’s a RE that uses re.VERBOSE; see how much easier it is to read?

```Python
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)
```

Without the verbose setting, the RE would look like this:

```Python
charref = re.compile("&#(0[0-7]+"
                     "|[0-9]+"
                     "|x[0-9a-fA-F]+);")
```

In the above example, Python’s automatic concatenation of string literals has been used to break up the RE into smaller pieces, but it’s still more difficult to understand than the version using re.VERBOSE.

## More Pattern Power

In this section, we’ll cover some new metacharacters, and how to use *groups* to retrieve portions of the text that was matched.

### More Metacharacters

There are some metacharacters that we haven’t covered yet. Most of them will be covered in this section.

Some of the remaining metacharacters to be discussed are zero-width assertions. They don’t cause the engine to advance through the string; instead, they consume no characters at all, and simply succeed or fail. For example, `\b` is an assertion that the current position is located at a word boundary; the position isn’t changed by the `\b` at all. This means that zero-width assertions should never be repeated, because if they match once at a given location, they can obviously be matched an infinite number of times.

* `|`
    Alternation, or the “or” operator. If *A* and *B* are regular expressions, `A|B` will match any string that matches either *A* or *B*. `|` has very low precedence in order to make it work reasonably when you’re alternating multi-character strings.
    To match a literal `'|'`, use `\|`, or enclose it inside a character class, as in `[|]`.
* `^`
    Matches at the beginning of lines. Unless the MULTILINE flag has been set, this will only match at the beginning of the string. In MULTILINE mode, this also matches immediately after each newline within the string.
    To match a literal `'^'`, use `\^`.
* `$`
    Matches at the end of a line, which is defined as either the end of the string, or any location followed by a newline character.
    To match a literal `'$'`, use `\$` or enclose it inside a character class, as in `[$]`.
* `\A`
    Matches only at the start of the string. When not in MULTILINE mode, `\A` and `^` are effectively the same. In MULTILINE mode, they’re different: `\A` still matches only at the beginning of the string, but `^` may match at any location inside the string that follows a newline character.
`\Z`
    Matches only at the end of the string.
`\b`
    Word boundary. This is a zero-width assertion that matches only at the beginning or end of a word. A word is defined as a sequence of alphanumeric characters, so the end of a word is indicated by whitespace or a non-alphanumeric character.
    The following example matches class only when it’s a complete word; it won’t match when it’s contained inside another word.

    ```sh
    >>> p = re.compile(r'\bclass\b')
    >>> print(p.search('no class at all'))
    <re.Match object; span=(3, 8), match='class'>
    >>> print(p.search('the declassified algorithm'))
    None
    >>> print(p.search('one subclass is'))
    None
    ```

    There are two subtleties you should remember when using this special sequence. First, this is the worst collision between Python’s string literals and regular expression sequences. In Python’s string literals, `\b` is the backspace character, ASCII value 8. If you’re not using raw strings, then Python will convert the `\b` to a backspace, and your RE won’t match as you expect it to. The following example looks the same as our previous RE, but omits the 'r' in front of the RE string.
    Second, inside a character class, where there’s no use for this assertion, `\b` represents the backspace character, for compatibility with Python’s string literals.
* `\B`
    Another zero-width assertion, this is the opposite of `\b`, only matching when the current position is not at a word boundary.

### Grouping

Frequently you need to obtain more information than just whether the RE matched or not. Regular expressions are often used to dissect strings by writing a RE divided into several subgroups which match different components of interest. For example, an RFC-822 header line is divided into a header name and a value, separated by a `':'`, like this:

```txt
From: author@example.com
User-Agent: Thunderbird 1.5.0.9 (X11/20061227)
MIME-Version: 1.0
To: editor@example.com
```

This can be handled by writing a regular expression which matches an entire header line, and has one group which matches the header name, and another group which matches the header’s value.

Groups are marked by the `'('`, `')'` metacharacters. `'('` and `')'` have much the same meaning as they do in mathematical expressions; they group together the expressions contained inside them, and you can repeat the contents of a group with a quantifier, such as `*`, `+`, `?`, or `{m,n}`. For example, `(ab)*` will match zero or more repetitions of `ab`.

```sh
>>> p = re.compile('(ab)*')
>>> print(p.match('ababababab').span())
(0, 10)
```

Groups indicated with `'('`, `')'` also capture the starting and ending index of the text that they match; this can be retrieved by passing an argument to group(), start(), end(), and span(). Groups are *numbered starting with 0*. *Group 0 is always present; it’s the whole RE*, so [match object](https://docs.python.org/3/library/re.html#match-objects) methods all have group 0 as their default argument.

```sh
>>> p = re.compile('(a)b')
>>> m = p.match('ab')
>>> m.group()
'ab'
>>> m.group(0)
'ab'
```

*Subgroups are numbered from left to right, from 1 upward.* Groups can be nested; to determine the number, just count the opening parenthesis characters, going from left to right.

```sh
>>> p = re.compile('(a(b)c)d')
>>> m = p.match('abcd')
>>> m.group(0)
'abcd'
>>> m.group(1)
'abc'
>>> m.group(2)
'b'
```

group() can be passed multiple group numbers at a time, in which case it will return a *tuple* containing the corresponding values for those groups.

```sh
>>> m.group(2,1,2)
('b', 'abc', 'b')
```

The [groups()](https://docs.python.org/3/library/re.html#re.Match.groups) method returns a tuple containing the strings for all the subgroups, from *1* up to however many there are.

```sh
>>> m.groups()
('abc', 'b')
```

**Backreferences** in a pattern allow you to specify that the contents of an earlier capturing group must also be found at the current location in the string. For example, `\1` will succeed if the *exact* contents of group 1 can be found at the current position, and fails otherwise. Remember that Python’s string literals also use a backslash followed by numbers to allow including arbitrary characters in a string, so be sure to use a raw string when incorporating backreferences in a RE.

For example, the following RE detects doubled words in a string.

```sh
>>> p = re.compile(r'\b(\w+)\s+\1\b')
>>> p.search('Paris in the the spring').group()
'the the'
```

Backreferences like this aren’t often useful for just searching through a string — there are few text formats which repeat data in this way — but you’ll soon find out that they’re very useful when performing string substitutions.

### Non-capturing and Named Groups

