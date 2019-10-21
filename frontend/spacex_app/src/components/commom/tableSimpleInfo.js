import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const useStyles = makeStyles({
  root: {
    width: '100%',
    overflowX: 'auto',
  },
  table: {
    minWidth: 650,
  },
});

export default function TableInfor(props) {
  const classes = useStyles();
  const dataLaunche = props.dataLaunche

  return (
    <Paper className={classes.root}>
      <Table className={classes.table} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Informações</TableCell>
            <TableCell align="right"></TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          <TableRow key={dataLaunche.flight_number}>
            <TableCell component="th" scope="row">
              Flight Number
            </TableCell>
            <TableCell align="right">{dataLaunche.flight_number}</TableCell>
          </TableRow>
          <TableRow key={dataLaunche.launch_year}>
            <TableCell component="th" scope="row">
              Launch Year
            </TableCell>
            <TableCell align="right">{dataLaunche.launch_year}</TableCell>
          </TableRow>
          <TableRow key={dataLaunche.launch_date_unix}>
            <TableCell component="th" scope="row">
              Launch Date Unix
            </TableCell>
            <TableCell align="right">{dataLaunche.launch_date_unix}</TableCell>
          </TableRow>
          <TableRow key={dataLaunche.launch_date_utc}>
            <TableCell component="th" scope="row">
              Launch Date Utc
            </TableCell>
            <TableCell align="right">{dataLaunche.launch_date_utc}</TableCell>
          </TableRow>
          <TableRow key={dataLaunche.launch_date_local}>
            <TableCell component="th" scope="row">
              Launch Date Local
            </TableCell>
            <TableCell align="right">{dataLaunche.launch_date_local}</TableCell>
          </TableRow>
          <TableRow key={dataLaunche.is_tentative}>
            <TableCell component="th" scope="row">
              Is Tentative
            </TableCell>
            <TableCell align="right">{dataLaunche.is_tentative}</TableCell>
          </TableRow>
          <TableRow key={dataLaunche.tentative_max_precision}>
            <TableCell component="th" scope="row">
              Tentative Max Precision
            </TableCell>
            <TableCell align="right">{dataLaunche.tentative_max_precision}</TableCell>
          </TableRow>
          <TableRow key={dataLaunche.launch_success}>
            <TableCell component="th" scope="row">
              Launch Success
            </TableCell>
            <TableCell align="right">{dataLaunche.launch_success}</TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </Paper>
  );
}
