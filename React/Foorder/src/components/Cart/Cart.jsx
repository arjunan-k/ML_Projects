import classes from './Cart.module.css'
import Modal from '../UI/Modal'
import CartContext from '../../store/cart-context'
import { useContext, useState, Fragment } from 'react';
import CartItem from './CartItem';
import CheckOut from './CheckOut';

const Cart = props => {
    const cartCtx = useContext(CartContext)
    const [isCheckOut, setIsCheckOut] = useState(false)
    const [isSubmitting, setIsSubmitting] = useState(false)
    const [didSubmit, setDidSubmit] = useState(false)

    const totalAmount = `$${cartCtx.totalAmount.toFixed(2)}`

    const hasItems = cartCtx.items.length > 0

    const cartItemRemoveHandler = id => {
        cartCtx.removeItem(id)
    }

    const cartItemAddHandler = item => {
        cartCtx.addItem({...item, amount:1})
    }

    const OrderHandler = () => {
        setIsCheckOut(true)
    }

    const submitOrderHandler = async (userData) => {
        setIsSubmitting(true);
        await fetch('https://foorder-b7b3a-default-rtdb.firebaseio.com/orders.json', {
            method: 'POST',
            body: JSON.stringify({
                users: userData,
                orderedItems: cartCtx.items,
            })
        })
        
        setIsSubmitting(false)
        setDidSubmit(true)
        cartCtx.clearCart();
        
    }

    const cartItems = (
        <ul className={classes['cart-items']}>
            {cartCtx.items.map(item => 
                <CartItem 
                    key={item.id} 
                    name={item.name} 
                    amount={item.amount}
                    price={item.price} 
                    onRemove={cartItemRemoveHandler.bind(null, item.id)} 
                    onAdd={cartItemAddHandler.bind(null, item)} />)}
        </ul>
    )

    const modalActions = (
        <div className={classes.actions}>
        <button className={classes["button--alt"]} onClick={props.onHideCart}>Close</button>
        {hasItems && <button className={classes.button} onClick={OrderHandler}>Order</button>}
        </div>
    )

    const cartModalContent = <Fragment>
        {cartItems}
        <div className={classes.total}>
            <span>Total Amount</span>
            <span>{totalAmount}</span>
        </div>
        {isCheckOut && <CheckOut onConfirm={submitOrderHandler} onHideCart={props.onHideCart} />}
        {!isCheckOut && modalActions}
    </Fragment>

    const isSubmittingModalContent = <p>Sending order data...</p>

    const didSubmittingModalContent = <Fragment>
        <p>Successfully send the order!</p>
        <div className={classes.actions}>
        <button className={classes.button} onClick={props.onHideCart}>Close</button>
        </div>

    </Fragment>
    
    return (
        <Modal onHideCart={props.onHideCart}>
            {!isSubmitting && !didSubmit && cartModalContent}
            {isSubmitting && isSubmittingModalContent}
            {!isSubmitting && didSubmit && didSubmittingModalContent}
        </Modal>
    )
}

export default Cart;