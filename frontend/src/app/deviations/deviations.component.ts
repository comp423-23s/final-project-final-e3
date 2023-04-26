import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { Observable } from 'rxjs';
import { isAuthenticated } from '../gate/gate.guard';
import{ Reservations, ReservationsService, Room } from 'src/app/reservations.service'
import { AvailableTimes, Schedule, TimesService } from '../times.service';
import { Form, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-deviations',
  templateUrl: './deviations.component.html',
  styleUrls: ['./deviations.component.css']
})
export class DeviationsComponent {
  public static Route: Route = {
    path: 'deviations',
    component: DeviationsComponent, 
    title: 'deviations', 
  };

  public newDeviationsForm = this.formBuilder.group({
    new_start_time: '',
    new_end_time: '',
    new_time_interval: '',
  });


  constructor(protected formBuilder: FormBuilder, protected reservationService: ReservationsService) {
  }

  onSubmit(): void {
    
    let form = this.newDeviationsForm.value;
    
    let start_time = form.new_start_time ?? "";
    let end_time = form.new_end_time ?? "";
    let time_intertal = form.new_time_interval ?? "";
    
  }

}
