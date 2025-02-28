import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common'; 
import { HttpClientModule } from '@angular/common/http'; 
import { FormsModule } from '@angular/forms'; // Import FormsModule here

@Component({
  selector: 'app-root',
  standalone: true, 
  imports: [CommonModule, HttpClientModule, FormsModule], // Add FormsModule here
  template: `
<div class="container">
  <h1>Sistema de Contas</h1>
  
  <!-- Formulário de Criação -->
  <div class="form-section">
    <h2>Criar Novo Usuário</h2>
    <input [(ngModel)]="newUser.name" placeholder="Nome">
    <input [(ngModel)]="newUser.email" placeholder="Email">
    <button (click)="createUser()">Criar Usuário</button>
  </div>

  <!-- Listagem -->
  <div class="actions">
    <button (click)="getUsers()">Atualizar Lista</button>
    <button (click)="getAccount(1)">Ver Saldo Exemplo</button>
  </div>

  <!-- Exibição -->
  <div *ngIf="response">
    <pre>{{ response | json }}</pre>
  </div>
</div>
  `,
  styles: [`
.container {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
}

.form-section {
  margin-bottom: 30px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

input {
  display: block;
  margin: 10px 0;
  padding: 8px;
  width: 200px;
}

button {
  margin-right: 10px;
  padding: 8px 15px;
  cursor: pointer;
}
  `]
})
export class AppComponent {
  response: any;
  newUser: { name: string; email: string } = { name: '', email: '' };

  constructor(private http: HttpClient) {}

  getUsers() {
    this.http.get('http://localhost:8000/gateway/users').subscribe(res => this.response = res);
  }

  getAccount(id: number) {
    this.http.get(`http://localhost:8000/gateway/account/${id}`).subscribe(res => this.response = res);
  }

  createTestData() {
    this.http.post('http://localhost:8001/api/users/', {
      name: "Teste", 
      email: "teste@email.com"
    }).subscribe();
  }

  createUser() {
    this.http.post('http://localhost:8000/gateway/users', this.newUser)
      .subscribe(() => {
        this.getUsers(); // Atualiza a lista após criar
        this.newUser = { name: '', email: '' }; // Limpa o formulário
      });
  }
}
