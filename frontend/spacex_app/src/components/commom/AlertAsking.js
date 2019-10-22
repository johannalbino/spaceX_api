import React from 'react'
import { makeStyles } from '@material-ui/core/styles';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import Button from '@material-ui/core/Button';
import Slide from '@material-ui/core/Slide';

const Transition = React.forwardRef(function Transition(props, ref) {
  return <Slide direction="up" ref={ref} {...props} />;
});

function AlertAsking({onConfirm, title, description, show, setShow, archives}){

    const useStyles = makeStyles(theme => ({
        modalBody: {
          padding: "30px 0",
          textAlign: "center",
          fontSize: "20px",
          fontWeight: "700"
        },
        textBody: {
          float: "right",
          padding: "3px 15px",
        }
      }))

    const handleClose = () => {
        setShow(false)
    };
    const handleOnConfirm = (archives) => {
        onConfirm(true, archives)
    }

    const classes = useStyles()
    return  (
      <React.Fragment>
        <Dialog
        open={show}
        onClose={handleClose}
        aria-labelledby="alert-dialog-slide-title"
        aria-describedby="alert-dialog-slide-description"
      >
        <DialogTitle id="alert-dialog-slide-title" className={classes.modalBody}>{title}</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-slide-description" className={classes.textBody}>
            {description}
          </DialogContentText>
        </DialogContent>
        <DialogActions>
            <Button onClick={handleClose} color="primary">
                Cancelar
            </Button>
            <Button 
            onClick={() => handleOnConfirm(archives)}
            color="primary"
            >
            Confirmar
          </Button>
        </DialogActions>
      </Dialog>
      </React.Fragment>
    )
}

export default AlertAsking