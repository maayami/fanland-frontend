import React, { useState } from "react";
import { useHistory, useLocation, Link } from "react-router-dom";
import { useAuth } from "./useAuth";

export default function SignUp() {
  const [userName, setUserName] = useState("");
  let history = useHistory();
  let location = useLocation();
  let auth = useAuth();

  let { from } = location.state || { from: { pathname: "/auth/signin" } };

  const signup = () => {
    auth.signup(userName, () => {
      history.replace(from);
    });
  };

  const onTextChange = (e) => {
    setUserName(e.target.value);
  };
  return (
    <div>
      Signup
      <form onSubmit={signup}>
        <input onChange={onTextChange} />
        <input type="submit" value="SignUp" />
      </form>
      <Link to="/signin">SignIn</Link>
    </div>
  );
}
