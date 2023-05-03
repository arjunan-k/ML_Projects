import MainNavigation from "../components/MainNavigation";

function ErrorPage() {
    return (
        <>
            <MainNavigation />
            <main>
                <h1>An Error Occured</h1>
                <p>Couldn't find the page.</p>
            </main>
        </>
    )
}

export default ErrorPage;