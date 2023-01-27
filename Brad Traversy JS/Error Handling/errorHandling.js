const user = {email: 'john@gmail.com'};

try {
    // Reference Error
    // myFunction();

    // Type Error
    // null.myFunction();


    // Syntax Error
    // eval('Hello World')

    // URI Error
    // decodeURIComponent('%')

    // Creating Own Error
    if(!user.name) {
        // throw 'My Own Error';
        throw new SyntaxError('User has no name')
    }

} catch(e) {
    console.log(e)
    // console.log(e.message)
    // console.log(e.name)
    // console.log(e instanceof TypeError)

} finally {
    console.log('Finally run all time')
}

console.log('My Outside Code Continue')