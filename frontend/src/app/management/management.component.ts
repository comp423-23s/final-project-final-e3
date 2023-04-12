import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { Observable } from 'rxjs';
import { isAuthenticated } from '../gate/gate.guard';
import { ReservationsService, Room } from '../reservations.service';
import { ReservationsComponent } from '../reservations/reservations.component';
import { ManagementService } from '../management.service';

@Component({
  selector: 'app-management',
  templateUrl: './management.component.html',
  styleUrls: ['./management.component.css']
})
export class ManagementComponent {
  public static Route: Route = {
    path: 'management',
    component: ManagementComponent, 
    title: 'Management', 
    canActivate: [isAuthenticated], 
  };

  public rooms$: Observable<Room[]>;

  constructor(private reservationService: ReservationsService, private managementService: ManagementService){
    this.rooms$ = reservationService.list_of_rooms();
  }

  onClick(roomName: string): void {
    this.managementService
          .deleteRoom(roomName)
          .subscribe({
            next: (room) => this.onSuccess(room)
          });
  }

  onSuccess(room: Room): void {
    window.alert('Room ${room.name} has been deleted');
    window.location.reload();
  }
}
