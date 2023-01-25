class Github {
    constructor() {
        this.client_id = "your app oauth id";
        this.client_secret = "your app oauth secret"
        this.repos_count = 10;
        this.repos_sort = 'created: asc'
    }

    async getUser(user) {
        // const profileResponse = await fetch(`https://api.github.com/users/${user}?client_id=${this.client_id}&client_secret=${this.client_secret}`)
        // const repoResponse = await fetch(`https://api.github.com/users/${user}/repos?per_page=${this.repos_count}&sort=${this.repos_sort}&client_id=${this.client_id}&client_secret=${this.client_secret}`)


        const profileResponse = await fetch(`https://api.github.com/users/${user}`)
        const repoResponse = await fetch(`https://api.github.com/users/${user}/repos?per_page=${this.repos_count}&sort=${this.repos_sort}`)

        const profile = await profileResponse.json()
        const repo = await repoResponse.json()

        return {
            profile, repo
        }
    }
}