import React from 'react';
import TablePagination from '@material-ui/core/TablePagination';
import IconButton from '@material-ui/core/IconButton';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import KeyboardArrowLeft from '@material-ui/icons/KeyboardArrowLeft';
import KeyboardArrowRight from '@material-ui/icons/KeyboardArrowRight';
import { makeStyles } from '@material-ui/core/styles';
import range from 'lodash/range';

const useStyles = makeStyles(theme => ({
  root: {
    display: 'flex',
    color: theme.palette.text.secondary,
    marginLeft: theme.spacing(2.5)
  },
  list: {
    display: 'flex',
    padding: 0,
    fontFamily: '"Arial"'
  },
  pagination: {
    marginTop: 20
  }
}));

function TablePaginationActions({ count, page, rowsPerPage, onChangePage }) {
  const classes = useStyles();
  const pages = range(1, Math.ceil(count / rowsPerPage) + 1);

  return (
    <div className={classes.root}>
      <IconButton
        onClick={() => onChangePage(page - 1)}
        disabled={page === 0}
        aria-label="previous page"
      >
        <KeyboardArrowLeft />
      </IconButton>
      <List className={classes.list}>
        {pages.map((p, index) => (
          <ListItem
            button
            dense
            selected={p === page + 1}
            onClick={() => onChangePage(p - 1)}
            key={index}
          >
            {p}
          </ListItem>
        ))}
      </List>
      <IconButton
        onClick={() => onChangePage(page + 1)}
        disabled={page >= Math.ceil(count / rowsPerPage) - 1}
        aria-label="next page"
      >
        <KeyboardArrowRight />
      </IconButton>
    </div>
  );
}

function Pagination({
  itemsCount,
  pageSize,
  currentPage,
  onPageChange,
  onChangeRowsPerPage
}) {
  const classes = useStyles();
  return (
    <TablePagination
      rowsPerPageOptions={[10, 25, 50]}
      component="div"
      count={itemsCount}
      rowsPerPage={pageSize}
      labelRowsPerPage="Resultados por página"
      page={currentPage}
      onChangePage={onPageChange}
      labelDisplayedRows={() => ''}
      onChangeRowsPerPage={onChangeRowsPerPage}
      ActionsComponent={TablePaginationActions}
      classes={{ root: classes.pagination }}
    />
  );
}

export default Pagination;
