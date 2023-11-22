

### Functions references

|Functions      | Description                                               |
|---------------|-----------------------------------------------------------|
| fprintf       | Formats and writes data to a file handle.                   |
| scanf         | Reads formatted data from the standard input.               |
| strcmp        | Compares two strings and returns their relationship.        |
| strcpy        | Copies a string to another.                                 |
| strlen        | Returns the length of a string.                             |
| round         | Rounds a floating-point number to the nearest integer.      |
| max           | Returns the maximum value among the provided arguments.    |
| min           | Returns the minimum value among the provided arguments.    |
| sum           | Computes the sum of elements in an array or iterable.      |
| sorted        | Returns a sorted list of elements from an iterable.        |
| pow           | Raises a number to a specified power.                      |
| format        | Formats a specified value according to the given format.   |
| any           | Returns True if any element in an iterable is True.         |
| all           | Returns True if all elements in an iterable are True.       |
| enumerate     | Returns an enumerate object, providing index-value pairs.  |
| isdigit       | Checks if a character is a numeric digit.                   |
| isalpha       | Checks if a character is an alphabetic character.           |
| islower       | Checks if a character is a lowercase letter.                |
| isupper       | Checks if a character is an uppercase letter.               |
| isspace       | Checks if a character is a whitespace character.            |
| abs           | Returns the absolute value of a number.                     |
| bin           | Converts an integer to a binary string.                     |
| hex           | Converts an integer to a hexadecimal string.                |
| oct           | Converts an integer to an octal string.                     |
| reversed      | Returns a reverse iterator of a sequence.                   |
| abs_function  | Parses the absolute value function. Retrieves the absolute value of the expression within the parentheses.|                                                                         
| acos_function | Parses the arc cosine function. Retrieves the arc cosine (in radians) of the expression within the parentheses using the `math.acos` function.|                                    
| asin_function | Parses the arc sine function. Retrieves the arc sine (in radians) of the expression within the parentheses using the `math.asin` function.|                                         
| ceil_function | Parses the ceiling function. Retrieves the smallest integer greater than or equal to the expression within the parentheses using the `math.ceil` function.|                         
| exp_function  | Parses the exponential function. Retrieves the exponential value of the expression within the parentheses using the `math.exp` function.|                                          
| floor_function| Parses the floor function. Retrieves the largest integer less than or equal to the expression within the parentheses using the `math.floor` function.|                             
| log_function  | Parses the natural logarithm function. Retrieves the natural logarithm of the expression within the parentheses using the `math.log` function.|                                    
| max_function  | Parses the maximum function. Retrieves the maximum value among the expressions separated by commas within the parentheses using the `max` function.|                             
| min_function  | Parses the minimum function. Retrieves the minimum value among the expressions separated by commas within the parentheses using the `min` function.|
| pi_constant           | Returns the mathematical constant value of π (`math.pi`).                                                             |
| pow_function          | Retrieves the result of raising the `base` to the `exponent` using the `math.pow` function.                          |
| sqrt_function         | Retrieves the square root of the value within the parentheses using `math.sqrt`.                                      |
| tan_function          | Retrieves the tangent of the value within the parentheses using `math.tan`.                                           |
| addcslashes_function  | Adds backslashes in front of specified characters within the `text` based on the `unicode_escape` encoding.         |
| addslashes_function   | Adds backslashes in front of predefined characters (`\`, `'`, `"`) within the `text`.                                |
| bin2hex_function      | Converts ASCII characters within the `text` to hexadecimal values using `encode('utf-8').hex()`.                     |
| chop_function         | Removes whitespace or specified characters from the right end of a string (`text.rstrip()`).                         |
| chr_function          | Converts an ASCII code (`value`) to a character using `chr()`.                                                        | 
| chunk_split_function       | Splits `text` into chunks of length `chunk_len` and an optional final chunk of length `end`. Returns the chunks separated by newlines.|                                                
| convert_cyr_string_function| Converts `text` from the specified `from_charset` encoding to `to_charset` encoding using `encode().decode()`. Ignores errors during decoding.|                                    
| convert_uudecode_function  | Decodes `text` encoded in UUEncode format (`uu`) to UTF-8.|                                                                                                                            
| convert_uuencode_function  | Encodes `text` in UUEncode format (`uu`) from UTF-8.|                                                                                                                                   
| count_chars_function       | Generates a dictionary containing the count of each unique character in `text`.|                                                                                                       
| crc32_function             | Calculates the CRC32 checksum of `text` and returns it as a string in binary representation using `binascii.crc32()`.|                                                                 
| crypt_function             | Encrypts `text` using the `crypt` function with a randomly generated `salt`. Returns the hashed value.|                                                                                
| echo_function              | Outputs the values of the arguments passed within parentheses (`args`) to the standard output (`sys.stdout`). |                           
| explode_function                 | Splits `text` into a list using `delimiter` as the separator. Returns the list of substrings.|                                                                                    
| fprintf_function                 | Writes formatted output to the standard output (`sys.stdout`). Formats the `format_str` string with `args` using `%` operator and writes| 
| get_html_translation_table_function | Returns HTML translation tables (`codepoint2name` or `name2codepoint`) based on the specified `table_type` (1 or 2).|                                                         
| hebrev_function                  | Performs a logical Hebrew text reversal for `text` and returns the result.|                                                                                                         
| hebrevc_function                 | Performs a visual Hebrew text reversal for `text` and returns the result.|                                                                                                          
| hex2bin_function                 | Converts a hexadecimal string `hex_string` to its binary representation and returns it as a UTF-8 decoded string.|                                                                  
| html_entity_decode_function      | Decodes HTML entities (`&amp;`, `&lt;`, `&gt;`, etc.) in `text` and returns the decoded string.|                                                                                   
| htmlentities_function            | Converts special characters in `text` to HTML entities (`&amp;`, `&lt;`, `&gt;`, etc.) and returns the encoded string.|                                                            
| htmlspecialchars_decode_function | Decodes HTML special characters (`&amp;`, `&lt;`, `&gt;`, etc.) in `text` and returns the decoded string.|                                                                         
| htmlspecialchars_function        | Converts special characters in `text` to HTML entities (`&amp;`, `&lt;`, `&gt;`, etc.) and returns the encoded string.|
| implode_function                 | Joins elements of `elements` (a list or string) into a string using `separator` as the delimiter and returns the resulting string.| 
| lcfirst_function           | Converts the first character of `text` to lowercase.|                                                                                                                   
| levenshtein_function       | Computes the Levenshtein distance between `str1` and `str2`, measuring the minimum number of edits needed to transform one string into other| 
| localeconv_function        | Retrieves the current locale's numeric and monetary formatting information as a dictionary using `locale.localeconv()`.                                                
| ltrim_function             | Removes leading whitespace or specified characters from the left end of `text` using `text.lstrip()`.|                                                                 
| md5_function               | Calculates the MD5 hash of `text` and returns it as a hexadecimal string using `hashlib.md5()`.|                                                                      
| md5_file_function          | Calculates the MD5 hash of the content of the specified file (`filename`) and returns it as a hexadecimal string using `hashlib.md5()`.|                               
| metaphone_function         | Generates the metaphone key of `text`, a phonetic encoding of words, using the `metaphone()` function.|                                                               
| money_format_function      | Formats `value` as currency based on the format string (`format_str`) and current locale using `locale.currency()` with grouping enabled.|                               
| nl_langinfo_function       | Retrieves specific locale information (`item`) using `locale.nl_langinfo()`.|                                                                                            
| nl2br_function             | Replaces newline characters (`\n`) in `text` with HTML `<br>` tags followed by a newline (`<br>\n`).|                                                                 
| number_format_function     | Formats `number` as a string using specified decimal and thousand separators (`decimals`, `dec_point`, `thousands_sep`) and grouping.|
| ord_function               | Retrieves the ASCII value of the first character of `text` using `ord()`. Returns `None` if `text` is empty.                                                                                                        
| parse_str_function       | Parses the URL-encoded query string (`query`) into variables and returns them as a dictionary.                                   |
| print_function           | Prints the arguments (`args`) to the standard output (`sys.stdout`) without a newline at the end.                                 |
| printf_function          | Prints a formatted string (`format_str`) with provided arguments (`args`) to the standard output (`sys.stdout`).                 |
| quoted_printable_decode_function | Decodes a quoted-printable string (`text`) to its original content using `quopri.decodestring()`.                               |
| quoted_printable_encode_function | Encodes `text` in quoted-printable format using `quopri.encodestring()`.                                                         |
| quotemeta_function       | Escapes special characters in `text` using `re.escape()`.                                                                          |
| rtrim_function           | Removes trailing whitespace or specified characters from the right end of `text` using `text.rstrip()`.                         |
| setlocale_function       | Sets or queries the program's current locale (`locale_str`) for the specified category (`category`) using `locale.setlocale()`.   |
| sha1_function            | Calculates the SHA-1 hash of `text` and returns it as a hexadecimal string using `hashlib.sha1()`.                                |
| sha1_file_function       | Calculates the SHA-1 hash of the content of the specified file (`filename`) and returns it as a hexadecimal string.                |
| similar_text_function    | Calculates the similarity percentage between `str1` and `str2` using the `similar_text()` function.                               |
| soundex_function         | Generates the soundex key for `text` using the `soundex()` function.                                                               |
| sprintf_function         | Formats a string (`format_str`) with provided arguments (`args`) using string interpolation (`%` operator).                       |
| sscanf_function          | Parses input (`text`) according to the format string (`format_str`) using regular expression matching (`re.match()`).             |
| str_getcsv_function      | Parses CSV data in `text` and returns it as a list using the `csv.reader()` function.                                              |
| str_ireplace_function    | Replaces all occurrences of `search` in `subject` with `replace`, ignoring case sensitivity.                                       |
| str_pad_function         | Pads `text` to a specified `length` using `pad_string` based on the `pad_type` provided (left, right, or center alignment).      |
| str_repeat_function      | Repeats `text` `count` times.                                                                                                      |
| str_replace_function     | Replaces all occurrences of `search` in `subject` with `replace`.                                                                  |
| str_rot13_function         | Applies the ROT13 substitution cipher to `text`, replacing each letter with the letter 13 positions ahead in the alphabet.|                                  
| str_shuffle_function       | Shuffles the characters in `text` randomly and returns the shuffled string.|                                                                                                       
| str_split_function         | Splits `text` into a list of substrings using `delimiter` as the separator. Returns the list of substrings.|                                                                       
| str_word_count_function    | Counts the number of words in `text` using a regular expression to identify word boundaries.|                                                                                       
| strcasecmp_function        | Performs a case-insensitive string comparison between `str1` and `str2`. Returns `True` if the strings are equal ignoring case.|                                
| strchr_function            | Finds the position of the first occurrence of `search` in `text`. Returns the index of the start of the found substring.|
| strcmp_function            | Compares `str1` with `str2` and returns `True` if they are identical, `False` otherwise.|                                                                                            
| strcoll_function           | Performs a locale-specific string comparison between `str1` and `str2` using the `locale.strcoll()` function.|                                                                     
| strcspn_function           | Returns the length of the initial segment of `text` that does not contain any characters from `charlist`.|                                                                          
| strip_tags_function        | Removes HTML tags (`<...>`) from `text` using a regular expression and returns the cleaned string.|                                                                                  
| stripcslashes_function     | Decodes a string with backslashes (`\\`) to their original representation using `unicode_escape` encoding.|                                                                        
| stripslashes_function     | Removes backslashes (`\\`) from `text`.|                                                                                                                                           
| stripos_function           | Finds the position of the first occurrence of `needle` in `haystack`, ignoring case. Returns the index of the start of the found substring.|
| stristr_function              | Finds the first occurrence of `needle` in `haystack`, ignoring case, and removes it from `haystack`.|                                                                               
| strlen_function              | Returns the length of the `text` string.|                                                                                                                                           
| strnatcasecmp_function       | Performs a natural order case-insensitive string comparison between `str1` and `str2`.|                                                                                             
| strnatcmp_function           | Performs a natural order string comparison between `str1` and `str2`.|                                                                                                               
| strncasecmp_function         | Compares `n` characters of `str1` and `str2` case-insensitively. Returns `True` if the first `n` characters are equal, `False` otherwise.|                                          
| strncmp_function             | Compares the first `n` characters of `str1` and `str2`. Returns `True` if the first `n` characters are equal, `False` otherwise.|                                                   
| strpbrk_function             | Finds the position of the first occurrence of any character from `charlist` in `text`.|                                                                                              
| strpos_function              | Finds the position of the first occurrence of `needle` in `haystack`.|                                                                                                               
| strrchr_function             | Finds the last occurrence of `needle` in `haystack`.|                                                                                                                                
| strrev_function              | Reverses the characters in the `text` string.|                                                                                                                                       
| strripos_function            | Finds the last occurrence of `needle` in `haystack`, ignoring case.|                                                                                                                 
| strrpos_function             | Finds the last occurrence of `needle` in `haystack`.|                                                                                                                                
| strspn_function              | Returns the length of the initial segment of `text` that consists entirely of characters from `charlist`.|                                                                           
| strstr_function              | Finds the first occurrence of `needle` in `haystack` and returns the substring starting from that occurrence. |
| strtok_function              | Breaks a string `text` into smaller strings based on a specified `delimiter`.|                                                                                                       
| strtolower_function          | Converts the `text` string to lowercase.|                                                                                                                                            
| strtoupper_function          | Converts the `text` string to uppercase.|                                                                                                                                            
| strtr_function               | Replaces characters in `text` from `from_chars` to `to_chars` based on their positions.|                                                                                             
| substr_function              | Returns a portion of `text` starting from `start` with a length of `length`.|                                                                                                        
| substr_compare_function      | Compares substrings from `main_str` and `str` starting from `start` with a length of `length`. |                                                                                    
| substr_count_function        | Counts the number of occurrences of `substr` in `text`. |                                                                                                                            
| substr_replace_function      | Replaces a part of `text` specified by `start` and `length` with `replacement`.|                                                                                                    
| trim_function                | Removes whitespace or other specified characters from the beginning and end of `text`. |                                                                                             
| ucfirst_function             | Converts the first character of `text` to uppercase.|                                                                                                                                 
| ucwords_function             | Converts the first character of each word in `text` to uppercase.|                                                                                                                   
| vfprintf_function            | Writes a formatted string to a file pointer `stream`.|                                                                                                                                
| vprintf_function             | Outputs a formatted string.|                                                                                                                                                          
| vsprintf_function            | Returns a formatted string.|                                                                                                                                                         
| wordwrap_function            | Wraps a string `text` to a given number of characters `width`, optionally breaking long words. Returns the wrapped string.|                                                         







