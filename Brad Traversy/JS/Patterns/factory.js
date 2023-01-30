function MemberFactory() {
    this.createMember = function(name, type) {
        let member;
        if (type === 'simple') {
            member = new SimpleMemberShip(name)
        } 
        else if (type === 'standard') {
            member = new StandardMemberShip(name)
        }
        else if (type === 'super') {
            member = new SuperMemberShip(name);
        }

        member.type = type;

        member.define = function() {
            console.log(`${this.name} (${this.type}): ${this.cost}`)
        }

        return member
    }
}


const SimpleMemberShip = function(name) {
    this.name = name;
    this.cost = '$5'
}


const StandardMemberShip = function(name) {
    this.name = name;
    this.cost = '$15'
}


const SuperMemberShip = function(name) {
    this.name = name;
    this.cost = '$30'
}

const members = []
const factory = new MemberFactory()

members.push(factory.createMember('Appu', 'simple'))
members.push(factory.createMember('Brad', 'standard'))
members.push(factory.createMember('Neast', 'super'))

members.forEach(function(member) {
    member.define();
})