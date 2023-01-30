const Singleton = (function() {
    let instance;

    function createInstance() {
        const object = new Object({name: 'Brad'})
        return object
    }

    return {
        getInstance: function() {
            if(!instance) {
                instance = createInstance();
            }
            return instance
        }
    }

})();

const instanceA = Singleton.getInstance()
console.log(instanceA)

const instanceB = Singleton.getInstance()
console.log(instanceB)

console.log(instanceA === instanceB)