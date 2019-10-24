import React, { useEffect, useState } from 'react'
import { makeStyles } from '@material-ui/core/styles';
import { LaunchesTable } from './TableLaunches'
import { Grid } from '@material-ui/core';
import CircularProgress from '@material-ui/core/CircularProgress';
import Button from '@material-ui/core/Button'
import { postConsumptionAPI } from '../../services/launchesService'
import Link from '@material-ui/core/Link'


const useStyles = makeStyles(() => ({
    container: {
        padding: "0 10% 0 10%",
        position: "relative"
    },
    header: {
        textAlign: "center"
    },
    processUpload: {
        textAlign: "center",
        width: "100%",
    },
    button: {
        margin: "25px 0 0 0",
    },
    divButton: {
        textAlign: "right"
    },
    divTitle: {
        textAlign: "center"
    },
    table: {
        width: "100%",
        height: "100%"
    }
 }));

export default function Launches(){
    const [isLoading, setIsLoading] = useState(false)
    const [status, setStatus] = useState(true)
    const [msg, setMsg] = useState(true)
    const classes = useStyles()

    useEffect(() => {
        if (!status){
            console.log('oi')
        }
    })

    const handleUpdate = async () => {
        setIsLoading(true)
        try{
        const { data } = await postConsumptionAPI()
        setMsg(data.msg)
        }
        catch(error){
            setMsg(error)
        }
        setIsLoading(false)        
    }

    return(
        <React.Fragment>
            <Grid container className={classes.container}>
                <Grid item xs={4}>
                </Grid>
                <Grid item xs={4} className={classes.divTitle}>
                    <h1>Lançamentos</h1>
                </Grid>
                <Grid item xs={4} className={classes.divButton}>
                    <Link
                    onClick={() => handleUpdate()}
                    >
                        <Button variant="outlined" className={classes.button}>
                            Atualizar Dados
                        </Button>
                    </Link>
                </Grid>
                
                {isLoading?(
                    <div className={classes.processUpload}>
                        <CircularProgress size={100} />
                        <div>Processando...</div>
                        <div>Esse processo pode demorar até 10 minutos.</div>
                    </div>

                    ) : (
                        <Grid item xs={12}>
                            <LaunchesTable />
                        </Grid>
                )}
                
            </Grid>
        </React.Fragment>
    )
}

