import React, { useEffect, useState } from 'react'
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import { LaunchesTable } from './TableLaunches'
import { Grid } from '@material-ui/core';


const useStyles = makeStyles(() => ({
    container: {
        padding: "0 10% 0 10%"
    },
    header: {
        textAlign: "center"
    },
    table: {
        
    }
 }));

export default function Launches(){
    const [isLoading, setIsLoading] = useState(false)
    const classes = useStyles();

    return(
        <React.Fragment>
            <Grid container className={classes.container}>
                <Grid item xs={12} className={classes.header}>
                    <h1>Lançamentos</h1>
                </Grid>
                <Grid item xs={12} className={classes.table}>
                    <LaunchesTable /> 
                </Grid>
            </Grid>
        </React.Fragment>
    )
}

