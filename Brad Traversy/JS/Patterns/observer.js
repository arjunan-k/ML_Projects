function EventObserver() {
    this.observer = [];
}

EventObserver.prototype = {
    subcribe: function(fn) {
        this.observer.push(fn)
        console.log(`Subscribed to ${fn.name}`)
    },
    unsubscribe: function(fn){
        this.observer = this.observer.filter(function(item) {
            if (item !== fn) {
                return item;
            }
        })
        console.log(`Unsubscribed from ${fn.name}`)
    },
    fire: function() {
        this.observer.forEach(item => {
            item.call()
        })
    }
}

const click = new EventObserver();

document.querySelector('.sub-ms').addEventListener('click', function() {
    click.subcribe(getCurMS)
})

document.querySelector('.unsub-ms').addEventListener('click', function() {
    click.unsubscribe(getCurMS)
})

document.querySelector('.sub-s').addEventListener('click', function() {
    click.subcribe(getCurS)
})

document.querySelector('.unsub-s').addEventListener('click', function() {
    click.unsubscribe(getCurS)
})

document.querySelector('.fire').addEventListener('click', function() {
    click.fire();
})

const getCurMS = function() {
    console.log(`Current MS ${new Date().getMilliseconds()}`)
}

const getCurS = function() {
    console.log(`Current S ${new Date().getSeconds()}`)
}