import { useState } from "react";

import api from "../../services/api";

export default function Login() {

  const [email,setEmail] =
  useState("");

  const [password,setPassword] =
  useState("");

  const login = async () => {

    const response =
    await api.post(
      "/auth/login",
      {
        email,
        password
      }
    );

    localStorage.setItem(
      "token",
      response.data.token
    );

  };

  return (

    <div>

      <input
        placeholder="Email"
        onChange={(e)=>
          setEmail(e.target.value)
        }
      />

      <input
        type="password"
        placeholder="Password"
        onChange={(e)=>
          setPassword(e.target.value)
        }
      />

      <button onClick={login}>

        Login

      </button>

    </div>

  );

}