import { makeStyles } from "@material-ui/core";

const useStyles = makeStyles({
  container: {
    padding: "14px 18px",
  },
  logo: {
    marginBottom: "18px",
  },
  formPaper: {
    width: "300px",
    minHeight: "270px",
    borderColor: "rgba(0, 0, 0, 0.7)",
    boxShadow: "0px 0px 1px 1px rgb(25 24 24 / 17%) !important",
    padding: "20px 26px",
    display: "flex",
    flexDirection: "column",
  },
  heading1: {
    padding: "0px 0px",
    paddingBottom: "4px",
    margin: "0px 0px",
    marginBottom: "10px",
    textAlign: "left",
  },
  inputHeading: {
    textAlign: "left",
    fontFamily: "amazonText",
    fontWeight: "600",
    fontSize: "14px",
    marginBottom: "5px",
  },
  input: {
    padding: "3px 7px",
    height: "30px",
    borderRadius: "4px",
    border: "1px solid #a6a6a6",
    boxShadow: "0 1px 0 rgb(255 255 255 / 50%), 0 1px 0 rgb(0 0 0 / 7%) inset",
  },
});

export default useStyles;
