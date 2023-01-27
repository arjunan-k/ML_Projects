const data = [
    {title: "Appu", background: "software"},
    {title: "Arjun", background: "software nice"},
    {title: "Arun", background: "software consultant"}
]

function getdata() {
    output = ""
    setTimeout(() => {
        data.forEach(function(data, index){
            output += `<li>${data.title}</li>`
        })
        document.body.innerHTML = output;
    }, 1000);
}

function addData(newData) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            data.push(newData)
            let error = false
            if (!error) {
                resolve()
            } else {
                reject('Not Working')
            }
        }, 2000);
    })
}

// addData({title: "Anju Last", background: "Soft"}).then(getdata).catch(err => console.log(err))


async function loadAll() {
    await addData({title: "Anju Last", background: "Soft"})
    getdata()
}

loadAll()