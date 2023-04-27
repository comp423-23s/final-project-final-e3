import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { mergeMap, Observable, of, shareReplay } from 'rxjs';
import { Room } from './reservations.service';
import{Schedule} from './times.service'
import { ProfileService, Profile } from './profile/profile.service';

export interface Deviations {
  [date: string]: string[];
}

@Injectable({
  providedIn: 'root'
})
export class AddRoomService {
  public profile$: Observable<Profile| undefined>;
  public pid: number;

  constructor(protected http: HttpClient, protected profileService: ProfileService) { 
    this.profile$ = profileService.profile$;
    this.pid = 0;
    this.profile$.subscribe(profile => {
      if(profile) {
         console.log(profile.pid);
        this.pid = profile.pid
      } else {
       console.error("Profile does not exists")
     }
    })

  }

  create_room(room_name: string, room_capacity: number, week_schedule: Schedule) : Observable<Room> {
    let params = new HttpParams().set('user_pid', this.pid)
    let room: Room = {name: room_name, max_capacity: room_capacity, availability: week_schedule, deviations: {}}
    return this.http.post<Room>("/api/room", room, {params:params});
  }
  
  modify_room(room_name: string | undefined, deviations: Deviations){
    return this.http.post<Room>(`/api/room/edit/${room_name}`, deviations)
  }
  
}
