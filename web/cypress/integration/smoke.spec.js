describe('Smoke Test', () => {
  it('can view the homepage', () => {
    cy.visit('/')
    cy.contains('Time:')
  })
})