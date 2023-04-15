import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { Observable } from 'rxjs';
import { isAuthenticated } from '../gate/gate.guard';
import { ReservationsService, Room } from '../reservations.service';
import { ReservationsComponent } from '../reservations/reservations.component';
import { ManagementService } from '../management.service';
import { Form, FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-add-room',
  templateUrl: './add-room.component.html',
  styleUrls: ['./add-room.component.css']
})
export class AddRoomComponent {
  public static Route: Route = {
    path: 'add-room',
    component: AddRoomComponent, 
    title: 'add-room',  
  };

  // public newRoom: Room;

  // public newRoomForm = this.formBuilder.group({
  //   room_name: '',
  //   room_capacity: '',

  // });

  // constructor(route: ActivatedRoute, protected formBuilder: FormBuilder, protected profileService: ProfileService, protected snackBar: MatSnackBar) {
  //   const form = this.profileForm;
  //   form.get('room_name')?.addValidators(Validators.required);
  //   form.get('room_capacity')?.addValidators(Validators.required);
  //   form.get('email')?.addValidators([Validators.required, Validators.email, Validators.pattern(/unc\.edu$/)]);
  //   form.get('pronouns')?.addValidators(Validators.required);

  //   const data = route.snapshot.data as { profile: Profile };
  //   this.newRoom = data.profile;
  // }

  // ngOnInit(): void {
  //   let newRoom = this.newRoom;

  //   this.newRoom.setValue({
  //     first_name: profile.first_name,
  //     last_name: profile.last_name,
  //     email: profile.email,
  //     pronouns: profile.pronouns
  //   });
  // }

  // onSubmit(): void {
  //   if (this.newRoomForm.valid) {
  //     Object.assign(this.newRoom, this.newRoom.value)
  //     this.profileService.put(this.newRoom).subscribe(
  //       {
  //         next: (room) => this.onSuccess(room),
  //         error: (err) => this.onError(err)
  //       } 
  //     );
  //   }
  // }

  // private onSuccess(room: Room) {
  //   this.snackBar.open("Profile Saved", "", { duration: 2000 })
  // }

  // private onError(err: any) {
  //   console.error("How to handle this?");
  // }
}
