import React, { useEffect, useState } from 'react'
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import { LaunchesTable } from './TableLaunches'


const useStyles = makeStyles(() => ({
    
 }));

export default function Launches(){
    const [isLoading, setIsLoading] = useState(false)
    const classes = useStyles();

    return(
        <React.Fragment>
            <Container fixed>
                    <LaunchesTable />  
            </Container>  
        </React.Fragment>
    )
}

