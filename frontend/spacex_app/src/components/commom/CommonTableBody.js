import React from 'react';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import TableBody from '@material-ui/core/TableBody';

function CommonTableBody({ columns, data, valueProperty }) {
  const createKey = (item, column) =>
    item[valueProperty] + (column.path || column.key);

  const renderCell = (item, column) => {
    if (column.content) return column.content(item);
    return item[column.path];
  };

  return (
    <TableBody>
      {data.map((item, index) => (
        <TableRow key={index} hover>
          {columns.map(
            column =>
              column.display === true && (
                <TableCell key={createKey(item, column)}>
                  {renderCell(item, column)}
                </TableCell>
              )
          )}
        </TableRow>
      ))}
    </TableBody>
  );
}

export default CommonTableBody;
