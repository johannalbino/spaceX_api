import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';
import { Link } from 'react-router-dom'

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
    height: '64px'
  },
  logo: {
    flexGrow: 1
  },
  menu: {
    flexGrow: 1,
    display: 'none',
    [theme.breakpoints.up('md')]: {
      marginLeft: theme.spacing(1),
      display: 'block'
    }
  },
  listIcon: {
    [theme.breakpoints.up('lg')]: {
      marginLeft: theme.spacing(1),
      display: 'none'
    }
  },
}));

function Header() {
  const classes = useStyles();
  const itens = [
    {text: 'Launches', path: '/lauches'},
    {text: 'Latest Launches', path: '/lastest_launche'},
    {text: 'Next Launche', path:'/next_launche'}
  ];
  return (
    <div className={classes.root}>
      <AppBar color="inherit">
        <Toolbar>
          <div className={classes.logo}>
          </div>
          <div className={classes.menu}>
            {itens.map((item, index) => (
              <Link to={item.path}>
                <Button color="primary" key={index}>
                  {item.text}
                </Button>
              </Link>
            ))}
          </div>
          <IconButton
            className={classes.listIcon}
            aria-label="more"
            aria-controls="long-menu"
            aria-haspopup="true"
          >
            <MoreVertIcon />
          </IconButton>
        </Toolbar>
      </AppBar>
    </div>
  );
}

export default Header;
