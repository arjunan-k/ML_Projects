const github = new Github();
const ui = new UI();

const searchUser = document.getElementById('searchUser');
searchUser.addEventListener('keyup', (e) => {
    const userText = e.target.value
    if (userText !== "") {
        github.getUser(userText)
            .then(data => {
                // console.log(data)
                if(data.profile.message === "Not Found") {
                    // Show Alert
                    ui.showAlert('User not found', 'alert alert-danger')
                } else {
                    // Show Profile
                    ui.showProfile(data.profile)
                    ui.showRepos(data.repo)
                }
            })
            .catch(err => console.log(err))
    } else {
        // Clear Profile
        ui.clearProfile()
    }
});