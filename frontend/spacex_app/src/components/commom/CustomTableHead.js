import React from 'react';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import IconButton from '@material-ui/core/IconButton';
import TextField from '@material-ui/core/TextField';
import InputAdornment from '@material-ui/core/InputAdornment';
import Search from '@material-ui/icons/Search';
import Sort from '@material-ui/icons/Sort';
import { makeStyles } from '@material-ui/core/styles';
import { SelectInput } from './Inputs';

const useStyles = makeStyles({
  root: {
    width: 160
  },
  smallCell: {
    paddingTop: 0,
    paddingBottom: 20,
    paddingLeft: 0,
    paddingRight: 0
  }
});

function CustomTableHead({
  columns,
  filters,
  handleFilters,
  submitFilters,
  handleOrdering
}) {
  const renderCell = (
    column,
    filters,
    handleFilters,
    submitFilters,
    handleOrdering
  ) => {
    if (column.common) return column.label;
    if (!column.path) return;
    if (column.filter && column.filter.type === 'select') {
      return (
        <React.Fragment>
          <SelectInput
            name={filters[column.path]}
            value={filters[column.path]}
            label={column.label}
            options={column.filter.options}
            onChange={handleFilters(column.path, 'select')}
            className={classes.root}
            helperText={false}
          />
          <IconButton
            edge="end"
            onClick={() => handleOrdering(column.sortName || column.path)}
          >
            <Sort />
          </IconButton>
        </React.Fragment>
      );
    }
    return (
      <React.Fragment>
        <TextField
          classes={{ root: classes.root }}
          variant="outlined"
          type="text"
          label={column.label}
          placeholder="Pesquisar"
          InputLabelProps={{ shrink: true }}
          value={filters[column.path]}
          onChange={handleFilters(column.path)}
          InputProps={{
            endAdornment: (
              <InputAdornment position="end">
                <IconButton
                  edge="end"
                  aria-label={`filtrar por ${column.label}`}
                  onClick={submitFilters}
                >
                  <Search />
                </IconButton>
              </InputAdornment>
            )
          }}
        />
        <IconButton
          edge="end"
          onClick={() => handleOrdering(column.sortName || column.path)}
        >
          <Sort />
        </IconButton>
      </React.Fragment>
    );
  };

  const classes = useStyles();
  return (
    <TableHead>
      <TableRow>
        {columns.map(
          column =>
            column.display === true && (
              <TableCell
                size="small"
                align="left"
                key={column.path || column.key}
                classes={{ sizeSmall: classes.smallCell }}
              >
                {renderCell(
                  column,
                  filters,
                  handleFilters,
                  submitFilters,
                  handleOrdering
                )}
              </TableCell>
            )
        )}
      </TableRow>
    </TableHead>
  );
}

export default CustomTableHead;
