import React from "react";
import { Grid, Paper } from "@material-ui/core";
import useStyles from "./style";

const Login = () => {
  const classes = useStyles();
  return (
    <>
      <Grid
        container
        justifyContent="center"
        direction="column"
        className={classes.container}
      >
        <Grid item align="center" className={classes.logo}>
          amazon logo.
        </Grid>
        <Grid item align="center">
          <Paper className={classes.formPaper}>
            <h1 className={classes.heading1}>Sign in</h1>
            <button>click</button>
          </Paper>
        </Grid>
      </Grid>
    </>
  );
};

export default Login;
