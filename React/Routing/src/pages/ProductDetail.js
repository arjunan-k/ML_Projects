import { useParams, Link } from "react-router-dom";

function ProductDetailPage() {
    const params = useParams();
    const id = params.productId

    return (
        <>
            <h1>This is Product {id} details page.</h1>
            <Link to=".." relative="path">Back</Link>
        </>
    )
}

export default ProductDetailPage;