import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Room } from './reservations.service';
import { ProfileService, Profile } from './profile/profile.service';

@Injectable({
  providedIn: 'root'
})
export class ManagementService {

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

  deleteRoom(roomName: string): Observable<Room>
  {
    let params = new HttpParams().set('user_pid', this.pid)
    return this.http.delete<Room>(`/api/room/${roomName}`, {params: params})
  }

}