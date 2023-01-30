let re;

re = /hello/i          // Must need hello, i make case insensitive
re = /^h/i             // Must start with
re = /world$/i         // Must end with
re = /^hello$/i        // Must begin and end with
re = /^h...llo$/i      // Matches any Three character
re = /h*llo/i          // Matches any character 0 or more
re = /gra?e?y/         // Optional character
re = /gra?e?y\?/i      // Escape character


                       // Brackets [] - Character Sets

re = /gr[ae?]y/        // Must be a or e or ?
re = /[GF]ray/         // Must be G or F
re = /[^GF]ray/        // Match except G or F
re = /[A-Z]ray/        // Match any Upper Case
re = /[a-z]ray/        // Match any Lower Case
re = /[A-Za-z]ray/     // Match any Upper & Lower Case
re = /[0-9]/           // Match any digit


                       // Braces {} - Quantifiers

re = /Hel{2}o/i        // Must occur prefix alphabet exactly {m} times
re = /Hel{2,4}o/i      // Must occur prefix alphabet b/w {m, n} times
re = /Hel{2,}o/i       // Must occur prefix alphabet at least {m} times


                       // Parenthesis () - Grouping

re = /([0-9]x){3}/     // All inside () must repeat {m} times
re = /([0-9]x){3}$/    // All inside () must repeat {m} times and end with


                       // Shorthand Character Classes

re = /\w/              // Word Character - alphanumeric or _
re = /\w+/             // + looks for One or More
re = /\W/              // Non-Word Character
re = /\d/              // Match any Digit
re = /\D/              // Match any Non-Digit
re = /\s/              // Match Whitespace Char
re = /\S/              // Match Non-Whitespace Char
re = /Hell\b/i         // Word-Bountary, Exact position
re = /x(?=y)/          // Match x only if followed by y
re = /x(?!y)/          // Match x only if not followed by y


const str = "hello Hellxa"


function reTest(re, str) {
    if(re.test(str)) {
        console.log(`${str} matches ${re.source}`)
    } else {
        console.log(`${str} doesnot match ${re.source}`)
    }
}


const result = re.exec(str);
console.log(result)
reTest(re, str)