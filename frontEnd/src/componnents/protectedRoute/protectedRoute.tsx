import {Navigate} from "react-router"
import type { ReactNode } from "react";

type ProtectedRouteProps ={
    children : ReactNode 
}

export const ProtectedRoute = ({children }: ProtectedRouteProps) => {
    const user = localStorage.getItem("userName")
  if (!user) {
    return <Navigate to={"/enter"} replace />;
  }

  return children;
};