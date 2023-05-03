import { useNavigate } from "react-router-dom";

function HomePage() {
    const navigate = useNavigate()

    const buttonHandler = () => {
        navigate('products')
    }

    return (
        <>
            <h1>Home</h1>
            <button onClick={buttonHandler}>Go to Products</button>
        </>
    )
}

export default HomePage;