let re;
re = /hello/;
re = /hello/i;
// re = /hello/g;

console.log(re);
console.log(re.source);

// exec() - Return result in a array or null

const result = re.exec('AAhellodd world Hello');

console.log(result);
console.log(result[0]);
console.log(result.index);
console.log(result.input);

const result1 = re.test('Hello')
console.log(result1)

const str = 'Hello There';
const result2 = str.match(re)
console.log(result2)

const str1 = 'Hello there'
const result3 = str1.search(re)
console.log(result3)

const str2 = 'Hello There'
const newStr = str2.replace(re, 'Appu')
console.log(newStr)