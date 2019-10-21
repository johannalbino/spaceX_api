import React, { useState, useEffect } from 'react'
import Modal from 'react-bootstrap/Modal'
import 'bootstrap/dist/css/bootstrap.min.css'
import ButtonToolbar from 'react-bootstrap/ButtonToolbar'
import { MdCheckCircle, MdError, MdLink } from "react-icons/md"
import { makeStyles } from '@material-ui/core/styles';


function AlertComponent({props, smShow, setSmShow, msg}){
  const [check, setCheck] = useState(false)

  useEffect(() => {
    if(msg.includes('sucesso')){
      setCheck(true)
    }
    else{
      setCheck(false)
    }
  })

  const getColor = () =>{
    if (check){
      return '#007E7A'
    }
    return '#E57878'
  }

  const useStyles = makeStyles(theme => ({
    modalBody: {
      padding: "50px 20px 60px 20px",
      textAlign: "center",
      fontSize: "20px"
    },
    textBody: {
      float: "right",
      padding: "3px 15px",
      color: getColor()
    }
  }))
  
  const classes = useStyles();
    return  (
      <React.Fragment>
      <ButtonToolbar>

      <Modal
        size="md"
        show={smShow}
        onHide={() => setSmShow(false)}
        aria-labelledby="contained-modal-title-vcenter"
        centered
      >
        <Modal.Header closeButton>
        <Modal.Title id="example-modal-sizes-title-md">
        {check ? (
            <MdCheckCircle size={24} color={getColor()} />
          ) : (
            <MdError size={24} color={getColor()} />
          )
          }
          <div className={classes.textBody}>
          Alerta
          </div>
          </Modal.Title>
        </Modal.Header>
        <Modal.Body className={classes.modalBody}>
          {msg}
        </Modal.Body>
      </Modal>

    </ButtonToolbar>
      </React.Fragment>
    )
}

export default AlertComponent