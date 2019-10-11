import React from 'react'
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(() => ({
    gridContainer: {
      paddingTop: 15,
      paddingLeft: 10,
      paddingRight: 10,
      minHeight: 'calc(100% - 150px)',
      display: 'flex',
      flexDirection: 'row'
    }
 }));

export default function Launches(){
    const classes = useStyles();
    return(
        <React.Fragment>
            <div className={classes.gridContainer}>
                

            </div>
        </React.Fragment>
    )
}

