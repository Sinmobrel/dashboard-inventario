import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://localhost:8000/api/token/';  // Asegúrate de que esta URL sea correcta

  constructor(private http: HttpClient) { }

  login(username: string, password: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}`, { username, password });
  }

  refreshToken(refresh: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}refresh/`, { refresh });
  }
}
