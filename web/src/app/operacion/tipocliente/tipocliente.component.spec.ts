import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TipoclienteComponent } from './tipocliente.component';

describe('TipoclienteComponent', () => {
  let component: TipoclienteComponent;
  let fixture: ComponentFixture<TipoclienteComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TipoclienteComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TipoclienteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
