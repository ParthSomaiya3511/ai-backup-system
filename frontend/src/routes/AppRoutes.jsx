import {

    BrowserRouter,

    Routes,

    Route

} from "react-router-dom";

import Dashboard from "../pages/Dashboard/Dashboard";
import BackupCenter from "../pages/BackupCenter/BackupCenter";
import RecoveryCenter from "../pages/RecoveryCenter/RecoveryCenter";
import AIInsights from "../pages/AIInsights/AIInsights";
import Alerts from "../pages/Alerts/Alerts";
import Settings from "../pages/Settings/Settings";
import Login from "../pages/Login/Login";
import DeviceManagement from "../pages/DeviceManagement/DeviceManagement";
import OrganizationManagement from "../pages/OrganizationManagement/OrganizationManagement";
import AuditLogs from "../pages/AuditLogs/AuditLogs";
import UserManagement from "../pages/UserManagement/UserManagement"

export default function AppRoutes() {

    return (

        <BrowserRouter>

            <Routes>

                <Route

                    path="/login"

                    element={<Login />}

                />
                <Route
                    path="/"
                    element={<Dashboard />}
                />

                <Route path="/" element={<Dashboard />} />

                <Route path="/backup" element={<BackupCenter />} />

                <Route path="/recovery" element={<RecoveryCenter />} />

                <Route path="/ai" element={<AIInsights />} />

                <Route path="/alerts" element={<Alerts />} />

                <Route path="/settings" element={<Settings />} />

                <Route
                    path="/users"
                    element={<UserManagement />}
                />

                <Route
                    path="/devices"
                    element={<DeviceManagement />}
                />

                <Route
                    path="/organizations"
                    element={<OrganizationManagement />}
                />

                <Route
                    path="/audit"
                    element={<AuditLogs />}
                />

            </Routes>

        </BrowserRouter>

    );

}