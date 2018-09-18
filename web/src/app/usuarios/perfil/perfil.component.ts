import { Component, ViewChild, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { PerfilService } from './perfil.service';
import { RenderInput, FormComponent } from '../../shared';

@Component({
  template: '<router-outlet></router-outlet>'
})
export class PerfilComponent { }


@Component({
  templateUrl: './perfil.component.html'
})
export class EditPerfilComponent implements OnInit {

  form: FormGroup;
  columns: string[];
  renderinputs: RenderInput[];
  service = this._s;
  otro = false;
  deleteable = false;
  retur = false;
  @ViewChild('f') public _form: FormComponent;
  @ViewChild('multi') private _multi: any;
  nombre = item => `Para el(la) ${item.cargo__nombre} el ${item.unidad__nombre} es a: ${item.precio}`;

  constructor(
    private _fb: FormBuilder,
    private _s: PerfilService,
    private _rt: Router
  ) {
    this.form = this._fb.group({
      username: ['', Validators.required],
      first_name: ['', [Validators.required, Validators.minLength(3)]],
      last_name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]]
    });
    this.columns = ['col1', ];
    this.renderinputs = [
      {
        column: 'col1', title: 'Nombre de usuario', type: 'text', name: 'username'
      },
      { column: 'col1', title: 'Nombre', type: 'text', name: 'first_name' },
      { column: 'col1', title: 'Apellidos', type: 'text', name: 'last_name' },
      {
        column: 'col1', title: 'Correo', type: 'email', name: 'email'
      },
    ];
  }



  ngOnInit() {
    this._form.setReady(true);
    const user = JSON.parse(localStorage.getItem('user'));
    this.form.patchValue(user);
    this._form.setReady(false);
    // 1.us-east-2.compute.amazonaws.com:8081/perfil/detail/form/
    // Promise.all([this._s.list({}), this._multi.complete]).then(data => {
    //   const datos = data[0] as any;
    //   this._form.setItem(datos.object_list[0]);
    //   this._form.setReady(false);
    // });
    this._form.successful = data => {
      this._rt.navigate(['ususarios/perfil']);
    }
  }
}

