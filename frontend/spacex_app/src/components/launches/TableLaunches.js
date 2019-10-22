import React, { useState, useEffect } from 'react';
import CustomTableHead from '../commom/CustomTableHead';
import CommonTableBody from '../commom/CommonTableBody'
import Table from '@material-ui/core/Table';
import { makeStyles } from '@material-ui/core/styles';
import Pagination from '../commom/Pagination';
import { getLaunchesAll } from '../../services/launchesService'
import { CircularProgress } from '@material-ui/core';
import AlertComponent from '../commom/AlertAsking'


const useStyles = makeStyles(theme => ({
    icon: {
      '&:hover': {
        color: [theme.palette.primary.main]
      }
    },
    responsiveScroll: {
      overflowX: 'auto',
      overflow: 'auto',
      padding: 10,
      marginTop: 50
    }
  }));

export function LaunchesTable() {

    const [launches, setLaunches] = useState([]);
    const [currentPage, setCurrentPage] = useState(0);
    const [pageSize, setPageSize] = useState(10);
    const [pageTitle, setPageTitle] = useState();
    const [count, setCount] = useState(0);
    const [isLoading, setIsLoading] = useState(false);
    const [filters, setFilters] = useState({});
    const [msg, setMsg] = useState([])
    const [params, setParams] = useState({});
    const [smShow, setSmShow] = useState(false)
    const [columns, setColumns] = useState([
    { path: 'flight_number', label: 'Flight Number', display : true,  viewColumns: true },
    { path: 'mission_name', label: 'Mission Name', display : true,  viewColumns: true },
    { path: 'launch_date_unix', label: 'Launch Date Unix', display : true,  viewColumns: true },
    { path: 'launch_date_utc', label: 'Launch Date UTC', display : true,  viewColumns: true },
    { path: 'launch_date_local', label: 'Launch Date Local', display : true,  viewColumns: true },
    {
        path: 'is_tentative',
        label: 'Tentative',
        display : true,  
        viewColumns: true
    },
    {
        path: 'launch_success',
        label: 'Launch Success',
        display : true,  
        viewColumns: true,
    }
    ]);

    useEffect(() => {
        const fetchLaunches = async () => {
        setIsLoading(true);
        try {
            const { data } = await getLaunchesAll({
            page_size: pageSize,
            ...params
            });
            setLaunches(data.results);
            setCount(data.count);
        } catch (error) {
            alert(error);
        }
            setIsLoading(false);
        };
        fetchLaunches();
    }, [pageSize, params, smShow]);

  const handlePageChange = page => {
    setCurrentPage(page);
    setParams(params);
    setParams(oldValues => ({ ...oldValues, page: page + 1 }));
  };

  const handleFilters = (name, input) => event => {
    event.persist();
    if (input === 'select') {
      setParams(oldValues => ({
        ...oldValues,
        [name]: event.target.value,
        page: 1
      }));
    } else {
      setFilters(oldValues => ({
        ...oldValues,
        [name]: event.target.value,
        page: 1
      }));
    }
    setCurrentPage(0);
  };

  const submitFilters = () => {
    setParams(oldValues => ({
      ...oldValues,
      ...filters
    }));
  };

  const handleOrdering = name => {
    setParams(oldValues => {
      if (!oldValues.ordering) {
        return { ordering: name };
      }
      if (oldValues.ordering === name) {
        return { ordering: '-' + name };
      }
      return { ordering: name };
    });
  };

  const handleChangeRowsPerPage = event => {
    setPageSize(event.target.value);
    setCurrentPage(0);
  };

  const classes = useStyles();

  return (
    <React.Fragment>
      <AlertComponent msg={msg} smShow={smShow} setSmShow={setSmShow} />
      { isLoading  ?  (
        <div className={classes.modalLoad}>
          <CircularProgress />
        </div>
        
      ) : (
    <div style={{ position: 'relative' }} className={classes.responsiveScroll}>
      <Table size="small">
        <CustomTableHead
        columns={columns}
        filters={filters}
        handleFilters={handleFilters}
        submitFilters={submitFilters}
        handleOrdering={handleOrdering}
      />
      <CommonTableBody
        columns={columns}
        data={launches}
        valueProperty="id_launche"
      />
    </Table>
    <Pagination
      itemsCount={count}
      pageSize={pageSize}
      currentPage={currentPage}
      onPageChange={handlePageChange}
      onChangeRowsPerPage={handleChangeRowsPerPage}
    />
    </div>
    )
  }  
  </React.Fragment> 
  )
};