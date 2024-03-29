import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppTitleStrategy } from './app-title.strategy';
import { GateComponent } from './gate/gate.component';
import { HomeComponent } from './home/home.component';
import { ProfileEditorComponent } from './profile/profile-editor/profile-editor.component';
import { ReservationsComponent } from './reservations/reservations.component';
import { TimesComponent } from './times/times.component';
import { ManagementComponent } from './management/management.component';
import { AddRoomComponent } from './add-room/add-room.component';
import { StaffComponent } from './staff/staff.component';
import { MyreservationsComponent } from './myreservations/myreservations.component';
import {DeviationsComponent} from './deviations/deviations.component'

const routes: Routes = [
  HomeComponent.Route,
  ProfileEditorComponent.Route,
  ReservationsComponent.Route,
  TimesComponent.Route,
  ManagementComponent.Route,
  GateComponent.Route,
  AddRoomComponent.Route,
  StaffComponent.Route,
  MyreservationsComponent.Route,
  DeviationsComponent.Route,
  { path: 'admin', title: 'Admin', loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule) },
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {
    scrollPositionRestoration: 'enabled',
    anchorScrolling: 'enabled'
  })],
  exports: [RouterModule],
  providers: [AppTitleStrategy.Provider]
})
export class AppRoutingModule {}