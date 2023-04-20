import styles from './ErrorModal.module.css'
import Card from './Card';
import Button from './Button';
import Wrapper from '../Helper/Wrapper';
import ReactDOM from 'react-dom';

const Backdrop = (props) => {
    return <div className={styles.backdrop} onClick={props.onConfirm}></div>
}

const ModalOverlay = (props) => {
    return (
        <Card className={styles.modal}>
            <header className={styles.header}>
                <h2>{props.title}</h2>
            </header>
            <div className={styles.content}>
                <p>{props.message}</p>
            </div>
            <footer className={styles.actions}>
                <Button onClick={props.onConfirm}>Okay</Button>
            </footer>
        </Card>
    )
}

const ErrorModal = (props) => {

    return (
        <Wrapper>
            {ReactDOM.createPortal(<Backdrop onConfirm={props.onConfirm}/>, document.getElementById('backdrop'))}
            {ReactDOM.createPortal(<ModalOverlay title={props.title} message={props.message} onConfirm={props.onConfirm}/>, document.getElementById('modaloverlay'))}
        </Wrapper>
    )
}

export default ErrorModal;