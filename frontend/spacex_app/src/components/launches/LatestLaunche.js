import React, { useState, useEffect } from 'react'
import Container from '@material-ui/core/Container';
import { makeStyles } from '@material-ui/core/styles';
import { getLatestLaunche } from '../../services/launchesService'
import { Slide } from 'react-slideshow-image';
import TableSimpleInfo from '../commom/tableSimpleInfo'
import { Grid } from '@material-ui/core';



export default function LatestLaunche(){
    const [isLoading, setIsLoading] = useState(false)
    const [msg, setMsg] = useState([])
    const [smShow, setSmShow] = useState(false)
    const [dataLaunche, setDataLaunche] = useState([])
    const [images, setImages] =useState([])
    let image = []

    const useStyles = makeStyles(() => ({
        backgroundSize: "100px",
        sliderContainer: {
            width: "80%",
            margin: "auto"
        },
        eachSlide: {
            '& div': {
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                backgroundSize: "cover",
                height: "550px"
            },
            '& span': {
                padding: "20px",
                fontSize: "20px",
                background: "#efefef",
                textAlign: "center"
            }            
        },
        container: {
            padding: "0 10% 0 10%"
        },
        header: {
            textAlign: "center"
        }
    }));

    const properties = {
        duration: 5000,
        transitionDuration: 500,
        infinite: true,
        indicators: true,
        arrows: true,
        onChange: (oldIndex, newIndex) => {
          console.log(`slide transition from ${oldIndex} to ${newIndex}`);
        }
      }

    useEffect(() => {
        const fetchLaunches = async () => {
            setIsLoading(true)
            try{
                    const {data} = await getLatestLaunche()
                    setDataLaunche(data.results[0])
                    getImagesObject(data.results[0])
            }
            catch(error){
                alert(error)
            }
            setIsLoading(false)
        }
        fetchLaunches()
    }, [])

    function getImagesObject(dataLaunche){
        for(var a in dataLaunche){
            if (a === "links"){
                for (var b in dataLaunche[a]){
                    if (b === "flickr_images"){
                        for(var c in dataLaunche[a][b]){
                            for (var d in dataLaunche[a][b][c]){
                                image.push(dataLaunche[a][b][c][d])
                            }                        
                        }
                        setImages(image)
                        break;
                    }
                }
            }
        }
    }
    const classes = useStyles()
    return(
        <React.Fragment>
            <Grid container className={classes.container}>
                <Grid item xs={12} className={classes.header}>
                    <h1>{ dataLaunche['mission_name'] }</h1>
                </Grid>
                <Grid item xs={12}>
                <div className={classes.sliderContainer}>
                    <Slide {...properties}>
                        <div className={classes.eachSlide}>
                            <div style={{'backgroundImage': `url(${images[0]})`, 'backgroundSize': '100% 550px'}}></div>
                        </div>
                        <div className={classes.eachSlide}>
                            <div style={{'backgroundImage': `url(${images[1]})`, 'backgroundSize': '100% 550px'}}></div>
                        </div>
                        <div className={classes.eachSlide}>
                            <div style={{'backgroundImage': `url(${images[2]})`, 'backgroundSize': '100% 550px'}}></div>
                        </div>
                    </Slide>                                       
                </div>
                <TableSimpleInfo dataLaunche={dataLaunche} />
                </Grid>
            </Grid>            
        </React.Fragment>
    )
}

