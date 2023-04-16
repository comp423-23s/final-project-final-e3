import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { TimesService } from '../times.service';

@Component({
  selector: 'app-times',
  templateUrl: './times.component.html',
  styleUrls: ['./times.component.css']
})
export class TimesComponent {
  public static Route: Route = {
    path: 'times',
    component: TimesComponent, 
    title: 'Times', 
  };
}
