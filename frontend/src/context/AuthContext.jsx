import {
  createContext,
  useState
} from "react";

export const AuthContext =
createContext();

export function AuthProvider({

  children

}) {

  const [token] =
  useState(

    localStorage.getItem(
      "token"
    )

  );

  return (

    <AuthContext.Provider
      value={{ token }}
    >

      {children}

    </AuthContext.Provider>

  );

}