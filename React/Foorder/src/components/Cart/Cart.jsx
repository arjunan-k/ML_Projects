import classes from './Cart.module.css'
import Modal from '../UI/Modal'
import CartContext from '../../store/cart-context'
import { useContext, useState } from 'react';
import CartItem from './CartItem';
import CheckOut from './CheckOut';

const Cart = props => {
    const cartCtx = useContext(CartContext)
    const [isCheckOut, setIsCheckOut] = useState(false)

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
    
    return (
        <Modal onHideCart={props.onHideCart}>
            {cartItems}
            <div className={classes.total}>
                <span>Total Amount</span>
                <span>{totalAmount}</span>
            </div>
            {isCheckOut && <CheckOut onHideCart={props.onHideCart} />}
            {!isCheckOut && modalActions}

        </Modal>
    )
}

export default Cart;