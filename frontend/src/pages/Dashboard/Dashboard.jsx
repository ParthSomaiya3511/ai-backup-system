import MainLayout from "../../components/layout/MainLayout";

import StatsCard from "../../components/cards/StatsCard";

import BackupChart from "../../components/charts/BackupChart";

import RecentActivity from "../../components/activity/RecentActivity";

export default function Dashboard() {

  return (

    <MainLayout>

      <div className="grid grid-cols-4 gap-4">

        <StatsCard
          title="Protected Files"
          value="15420"
        />

        <StatsCard
          title="Backups"
          value="8520"
        />

        <StatsCard
          title="Threats"
          value="0"
        />

        <StatsCard
          title="Recovery Points"
          value="425"
        />

      </div>

      <div className="mt-10">

        <BackupChart />

      </div>

      <div className="mt-10">

        <RecentActivity />

      </div>

    </MainLayout>

  );

}