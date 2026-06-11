import { Link } from "react-router-dom";

export default function Sidebar() {

  return (

    <div className="w-64 h-screen bg-slate-900">

      <div className="p-6">

        AI Backup

      </div>

      <nav className="flex flex-col">

        <Link to="/">
          Dashboard
        </Link>

        <Link to="/backup">
          Backup Center
        </Link>

        <Link to="/recovery">
          Recovery Center
        </Link>

        <Link to="/ai">
          AI Insights
        </Link>

        <Link to="/alerts">
          Alerts
        </Link>

      </nav>

    </div>

  );

}