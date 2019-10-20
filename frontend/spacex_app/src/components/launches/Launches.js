import React, { useEffect, useState } from 'react'
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import TableLaunches from '../commom/tableLaunches'
import { getLaunchesAll } from '../../services/launchesService'


const useStyles = makeStyles(() => ({
    
 }));

export default function Launches(){
    const [isLoading, setIsLoading] = useState(false)
    const [msg, setMsg] = useState([])
    const [smShow, setSmShow] = useState(false)
    const [dataLaunche, setDataLaunche] = useState([])
    const [images, setImages] =useState([])
    const classes = useStyles();

    useEffect(() => {
        const fetchLaunches = async () => {
            setIsLoading(true)
            try{
                    const {data} = await getLaunchesAll()
                    setDataLaunche(data.results)
            }
            catch(error){
                alert(error)
            }
            setIsLoading(false)
        }
        fetchLaunches()
    }, [])

    return(
        <React.Fragment>
            <Container fixed>
                <TableLaunches launches={dataLaunche} />                
            </Container>  
        </React.Fragment>
    )
}

