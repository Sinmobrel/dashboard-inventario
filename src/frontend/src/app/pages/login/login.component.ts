import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  loginForm = new FormGroup({
    username: new FormControl('', [Validators.required]),
    password: new FormControl('', [Validators.required])
  });
  errorMessage: string | null = null;

  private apiUrl = 'http://localhost:8000/api/core';

  constructor(private http: HttpClient, private router: Router) {}

  onSubmit() {
    if (this.loginForm.valid) {
      const username = this.loginForm.value.username ?? '';
      const password = this.loginForm.value.password ?? '';
      this.http.post(`${this.apiUrl}/empresa-login/`, { username, password }).subscribe(
        (response: any) => {
          // Si la autenticación es exitosa, redirigir a la página de inicio
          this.router.navigate(['/home']);
        },
        error => {
          // Manejar errores de autenticación
          this.errorMessage = 'Invalid username or password';
        }
      );
    }
  }
}
